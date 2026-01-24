# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class BeautySalon(models.Model):
    _name = 'beauty.salon'
    _description = 'Beauty Salon'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'
    
    name = fields.Char(string='Salon Name', required=True, tracking=True)
    code = fields.Char(string='Salon Code', required=True, tracking=True, help='Unique code for the salon')
    active = fields.Boolean(string='Active', default=True, tracking=True)
    
    # Contact Information
    phone = fields.Char(string='Phone', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    website = fields.Char(string='Website')
    
    # Address Information
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    zip = fields.Char(string='ZIP')
    
    # Salon Details
    opening_time = fields.Float(string='Opening Time', help='Opening time in 24h format (e.g., 9.0 for 9:00 AM)')
    closing_time = fields.Float(string='Closing Time', help='Closing time in 24h format (e.g., 18.0 for 6:00 PM)')
    capacity = fields.Integer(string='Capacity', help='Maximum number of clients that can be served simultaneously')
    
    # Staff Management
    manager_id = fields.Many2one('beauty.salon.staff', string='Manager', domain="[('is_manager', '=', True)]")
    staff_ids = fields.Many2many('beauty.salon.staff', string='Staff Members', 
                                 help='Staff members assigned to this salon')
    
    # Services Offered
    service_ids = fields.Many2many('beauty.salon.service', string='Services Offered', 
                                   help='Services available at this salon')
    
    # Related Records
    client_ids = fields.One2many('beauty.salon.client', 'salon_id', string='Clients')
    appointment_ids = fields.One2many('beauty.salon.appointment', 'salon_id', string='Appointments')
    
    # Status
    status = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('maintenance', 'Under Maintenance'),
        ('temporary_closed', 'Temporarily Closed'),
    ], string='Status', default='open', tracking=True)
    
    # Additional Information
    description = fields.Text(string='Description')
    image = fields.Binary(string='Salon Image', attachment=True)
    
    # Computed Fields
    staff_count = fields.Integer(string='Staff Count', compute='_compute_staff_count', store=True)
    client_count = fields.Integer(string='Client Count', compute='_compute_client_count', store=True)
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count', store=True)
    service_count = fields.Integer(string='Service Count', compute='_compute_service_count', store=True)
    
    @api.depends('staff_ids')
    def _compute_staff_count(self):
        for salon in self:
            salon.staff_count = len(salon.staff_ids)
    
    @api.depends('client_ids')
    def _compute_client_count(self):
        for salon in self:
            salon.client_count = len(salon.client_ids)
    
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for salon in self:
            salon.appointment_count = len(salon.appointment_ids)
    
    @api.depends('service_ids')
    def _compute_service_count(self):
        for salon in self:
            salon.service_count = len(salon.service_ids)
    
    @api.constrains('code')
    def _check_unique_code(self):
        for salon in self:
            if self.search_count([('code', '=', salon.code), ('id', '!=', salon.id)]) > 0:
                raise ValidationError(_('Salon code must be unique!'))
    
    @api.constrains('opening_time', 'closing_time')
    def _check_opening_hours(self):
        for salon in self:
            if salon.opening_time and salon.closing_time:
                if salon.opening_time >= salon.closing_time:
                    raise ValidationError(_('Opening time must be before closing time!'))
    
    @api.constrains('capacity')
    def _check_capacity(self):
        for salon in self:
            if salon.capacity < 1:
                raise ValidationError(_('Capacity must be at least 1!'))
    
    def name_get(self):
        result = []
        for salon in self:
            name = f"{salon.name} ({salon.code})" if salon.code else salon.name
            result.append((salon.id, name))
        return result
    
    # Action Methods for Form View Buttons
    def action_open(self):
        self.write({'status': 'open'})
    
    def action_close(self):
        self.write({'status': 'closed'})
    
    def action_maintenance(self):
        self.write({'status': 'maintenance'})
    
    def action_temporary_close(self):
        self.write({'status': 'temporary_closed'})
    
    # Action Methods for Stat Buttons
    def action_view_staff(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Staff Members',
            'res_model': 'beauty.salon.staff',
            'domain': [('id', 'in', self.staff_ids.ids)],
            'view_mode': 'tree,form',
            'context': {'default_salon_ids': [(6, 0, [self.id])]},
        }
    
    def action_view_clients(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Clients',
            'res_model': 'beauty.salon.client',
            'domain': [('salon_id', '=', self.id)],
            'view_mode': 'tree,form',
            'context': {'default_salon_id': self.id},
        }
    
    def action_view_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'beauty.salon.appointment',
            'domain': [('salon_id', '=', self.id)],
            'view_mode': 'tree,form,calendar',
            'context': {'default_salon_id': self.id},
        }
    
    def action_view_services(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Services',
            'res_model': 'beauty.salon.service',
            'domain': [('id', 'in', self.service_ids.ids)],
            'view_mode': 'tree,form',
            'context': {'default_salon_ids': [(6, 0, [self.id])]},
        }