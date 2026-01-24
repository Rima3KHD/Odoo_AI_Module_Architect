from odoo import models, fields

class BeautySalonStaff(models.Model):
    _name = 'beauty_salon.staff'
    _description = 'Staff members working at the beauty salon'

    
    name = fields.Char("Staff Name", required=True)
    
    specialization = fields.Selection("Specialization")
    
    phone = fields.Char("Phone Number")
    
    email = fields.Char("Email Address")
    
    active = fields.Boolean("Active", required=True)
    