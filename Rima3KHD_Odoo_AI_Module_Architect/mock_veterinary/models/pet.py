from odoo import models, fields

class Pet(models.Model):
    _name = 'vet.pet'
    _description = 'Pet model'
    
    name = fields.Char("Pet Name", required=True)
    species = fields.Char("Species")
    category_id = fields.Many2one('vet.pet.category', string='Category')
    
    # Optional: Add related fields for easier access
    category_name = fields.Char(related='category_id.name', string='Category Name', store=True)