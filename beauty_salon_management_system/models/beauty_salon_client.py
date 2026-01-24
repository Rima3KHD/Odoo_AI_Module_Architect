from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BeautySalonClient(models.Model):
    _name = 'beauty.salon.client'
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
    
    # Salon relationship
    salon_id = fields.Many2one('beauty.salon', string='Salon', required=True, 
                               default=lambda self: self._default_salon_id())
    
    # Membership status
    membership_status = fields.Selection([
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ], string="Membership Status", default='regular')
    
    # Computed fields
    appointment_count = fields.Integer("Appointments", compute='_compute_appointment_count', store=False)
    
    def _default_salon_id(self):
        # Default to the first active salon if available
        salon = self.env['beauty.salon'].search([('active', '=', True)], limit=1)
        return salon.id if salon else False
    
    @api.depends()
    def _compute_appointment_count(self):
        for client in self:
            client.appointment_count = self.env['beauty.salon.appointment'].search_count([
                ('client_id', '=', client.id)
            ])