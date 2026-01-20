from odoo import models, fields

class PropertyOffer(models.Model):
    _name = 'real_estate.offer'
    _description = 'Represents a purchase offer made on a property.'

    
    property_id = fields.Many2one("Property", required=True)
    
    buyer_name = fields.Char("Buyer Name", required=True)
    
    offer_price = fields.Float("Offer Price", required=True)
    
    status = fields.Selection("Status", required=True)
    