from odoo import models, fields

class PetCategory(models.Model):
    _name = 'vet.pet.category'
    _description = 'Pet Category'
    
    name = fields.Char('Category Name', required=True)
    description = fields.Text('Description')
    active = fields.Boolean('Active', default=True)
    
    # Optional: parent category for hierarchy
    parent_id = fields.Many2one('vet.pet.category', string='Parent Category')
    child_ids = fields.One2many('vet.pet.category', 'parent_id', string='Subcategories')