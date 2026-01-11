from odoo import models, fields

class RealEstateProperty(models.Model):
    _name = 'real_estate.property'
    _description = 'Represents a real estate property listing.'

    
    name = fields.Char("Property Name", required=True)
    
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condominium'),
        ('land', 'Land'),
        ('commercial', 'Commercial')
    ], "Property Type", required=True)
    
    description = fields.Text("Description")
    
    address = fields.Char("Address", required=True)
    
    price = fields.Float("Price", required=True)
    
    bedrooms = fields.Integer("Bedrooms")
    
    bathrooms = fields.Integer("Bathrooms")
    
    area = fields.Float("Area (sq ft)")
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
        ('cancelled', 'Cancelled')
    ], "Status", required=True, default='draft')