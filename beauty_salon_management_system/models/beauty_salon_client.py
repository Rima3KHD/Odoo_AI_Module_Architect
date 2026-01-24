from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BeautySalonClient(models.Model):
    _name = 'beauty_salon.client'
    _description = 'Client or customer of the beauty salon'
    
    name = fields.Char("Client Name", required=True)
    phone = fields.Char("Phone Number")
    email = fields.Char("Email Address")
    address = fields.Text("Full Address")
    date_of_birth = fields.Date("Date of Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    notes = fields.Text("Client Notes")
    active = fields.Boolean("Active", default=True)
    create_date = fields.Datetime("Created On", readonly=True)
    
    # Computed fields
    appointment_count = fields.Integer("Appointments", compute='_compute_appointment_count', store=False)
    
    @api.depends()
    def _compute_appointment_count(self):
        for client in self:
            client.appointment_count = self.env['beauty_salon.appointment'].search_count([('client_id', '=', client.id)])
    
    def action_open_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Client Appointments',
            'res_model': 'beauty_salon.appointment',
            'view_mode': 'tree,form,calendar',
            'domain': [('client_id', '=', self.id)],
            'context': {'default_client_id': self.id},
        }
    
    @api.constrains('email')
    def _check_email_unique(self):
        for client in self:
            if client.email:
                existing = self.search([('email', '=', client.email), ('id', '!=', client.id)])
                if existing:
                    raise ValidationError("Email address must be unique per client.")
    
    @api.constrains('phone')
    def _check_phone_unique(self):
        for client in self:
            if client.phone:
                existing = self.search([('phone', '=', client.phone), ('id', '!=', client.id)])
                if existing:
                    raise ValidationError("Phone number must be unique per client.")