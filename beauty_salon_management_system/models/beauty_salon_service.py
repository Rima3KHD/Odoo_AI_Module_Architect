from odoo import models, fields

class BeautySalonService(models.Model):
    _name = 'beauty_salon.service'
    _description = 'Service offered by the salon (e.g., haircut, manicure)'
    
    name = fields.Char("Service Name", required=True)
    description = fields.Text("Service Description")
    duration = fields.Integer("Duration (minutes)", required=True)
    price = fields.Float("Price", required=True)
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