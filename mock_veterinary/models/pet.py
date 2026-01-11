from odoo import models, fields

class Pet(models.Model):
    _name = 'vet.pet'
    _description = 'Pet model'

    
    name = fields.Char("Pet Name", required=True)
    
    species = fields.Char("Species")
    