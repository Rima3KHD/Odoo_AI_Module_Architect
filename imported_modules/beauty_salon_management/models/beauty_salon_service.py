from odoo import models, fields

class BeautySalonService(models.Model):
    _name = 'beauty_salon.service'
    _description = 'Service catalog offered by the beauty salon'

    
    name = fields.Char("Service Name", required=True)
    
    category = fields.Selection("Service Category", required=True)
    
    duration = fields.Integer("Duration (minutes)", required=True)
    
    price = fields.Float("Price", required=True)
    
    description = fields.Text("Service Description")
    