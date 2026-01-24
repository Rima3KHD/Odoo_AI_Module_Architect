from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BeautySalonService(models.Model):
    _name = 'beauty.salon.service'
    _description = 'Service offered by the salon (e.g., haircut, manicure)'
    
    name = fields.Char("Service Name", required=True)
    description = fields.Text("Service Description")
    duration = fields.Integer("Duration (minutes)", required=True)
    price = fields.Float("Price", required=True)
    
    # Salon relationship
    salon_ids = fields.Many2many('beauty.salon', string='Available at Salons', 
                                 help='Salons where this service is offered')
    
    category = fields.Selection([
        ('hair', 'Hair Services'),
        ('nails', 'Nail Services'),
        ('skin', 'Skin Care'),
        ('makeup', 'Makeup'),
        ('spa', 'Spa & Massage'),
        ('other', 'Other')
    ], string="Service Category", default='other')
    
    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer("Sequence", default=10)
    
    # Computed fields
    appointment_count = fields.Integer("Appointments", compute='_compute_appointment_count', store=False)
    
    @api.depends()
    def _compute_appointment_count(self):
        for service in self:
            service.appointment_count = self.env['beauty.salon.appointment'].search_count([
                ('service_id', '=', service.id)
            ])
    
    @api.constrains('duration', 'price')
    def _check_service_values(self):
        for service in self:
            if service.duration <= 0:
                raise ValidationError("Duration must be greater than 0 minutes!")
            if service.price < 0:
                raise ValidationError("Price cannot be negative!")
    
    def name_get(self):
        result = []
        for service in self:
            name = f"{service.name} ({service.duration}min - ${service.price:.2f})"
            result.append((service.id, name))
        return result