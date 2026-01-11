from odoo import models, fields

class RealEstateProperty(models.Model):
    _name = 'real_estate.property'
    _description = 'Represents a real estate property for sale or rent.'

    
    name = fields.Char("Property Name", required=True)
    
    street = fields.Char("Street")
    
    city = fields.Char("City")
    
    zip = fields.Char("ZIP Code")
    
    price = fields.Float("Price", required=True)
    
    property_type = fields.Selection("Property Type", required=True)
    