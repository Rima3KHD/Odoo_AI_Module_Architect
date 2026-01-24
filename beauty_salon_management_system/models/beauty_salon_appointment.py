from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class BeautySalonAppointment(models.Model):
    _name = 'beauty.salon.appointment'
    _description = 'Scheduled appointment for a client'
    _order = 'appointment_date desc'
    
    name = fields.Char(string='Appointment Reference', compute='_compute_name', store=True, readonly=True)
    
    # Salon relationship
    salon_id = fields.Many2one('beauty.salon', string='Salon', required=True, 
                               default=lambda self: self._default_salon_id())
    
    client_id = fields.Many2one('beauty.salon.client', string='Client', required=True, ondelete='cascade')
    service_id = fields.Many2one('beauty.salon.service', string='Service', required=True)
    staff_id = fields.Many2one('beauty.salon.staff', string='Assigned Staff', required=True)
    appointment_date = fields.Datetime(string='Appointment Date & Time', required=True, default=lambda self: fields.Datetime.now())
    duration = fields.Integer(string='Duration (minutes)', required=True, default=60)
    end_date = fields.Datetime(string='End Date & Time', compute='_compute_end_date', store=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ], string='Status', default='draft', tracking=True)
    
    reason_for_cancel = fields.Text(string='Reason for Cancel', 
                                    help='Reason provided when appointment is cancelled.',
                                    readonly=True,
                                    states={'cancelled': [('readonly', False)]})
    
    notes = fields.Text(string='Additional Notes')
    active = fields.Boolean(string='Active', default=True)
    create_date = fields.Datetime(string='Created On', readonly=True)
    
    def _default_salon_id(self):
        # Default to the first active salon if available
        salon = self.env['beauty.salon'].search([('active', '=', True)], limit=1)
        return salon.id if salon else False
    
    @api.depends('appointment_date', 'duration')
    def _compute_end_date(self):
        for appointment in self:
            if appointment.appointment_date and appointment.duration:
                start_date = fields.Datetime.from_string(appointment.appointment_date)
                end_date = start_date + timedelta(minutes=appointment.duration)
                appointment.end_date = fields.Datetime.to_string(end_date)
            else:
                appointment.end_date = False
    
    @api.depends('client_id', 'appointment_date')
    def _compute_name(self):
        for appointment in self:
            if appointment.client_id and appointment.appointment_date:
                client_name = appointment.client_id.name or 'Unknown'
                date_str = fields.Datetime.context_timestamp(appointment, fields.Datetime.from_string(appointment.appointment_date)).strftime('%Y-%m-%d %H:%M')
                appointment.name = f"{client_name} - {date_str}"
            else:
                appointment.name = "New Appointment"
    
    @api.constrains('appointment_date', 'duration')
    def _check_appointment_date(self):
        for appointment in self:
            if appointment.appointment_date:
                appointment_datetime = fields.Datetime.from_string(appointment.appointment_date)
                if appointment_datetime < datetime.now():
                    raise ValidationError("Appointment date cannot be in the past!")
                
                # Check for overlapping appointments for the same staff
                overlapping_appointments = self.search([
                    ('staff_id', '=', appointment.staff_id.id),
                    ('appointment_date', '<', appointment.end_date),
                    ('end_date', '>', appointment.appointment_date),
                    ('id', '!=', appointment.id),
                    ('state', 'not in', ['cancelled', 'completed'])
                ])
                
                if overlapping_appointments:
                    raise ValidationError("This staff member already has an appointment scheduled during this time!")
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})
    
    def action_complete(self):
        self.write({'state': 'completed'})
    
    def action_reset(self):
        self.write({'state': 'draft'})