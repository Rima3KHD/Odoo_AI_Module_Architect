from odoo import models, fields

class BeautySalonClient(models.Model):
    _name = 'beauty_salon.client'
    _description = 'Client information for the beauty salon'

    
    name = fields.Char("Client Name", required=True)
    
    phone = fields.Char("Phone Number", required=True)
    
    email = fields.Char("Email Address")
    
    birth_date = fields.Date("Birth Date")
    
    notes = fields.Text("Notes")
    
    allergies = fields.Text("Allergies or Sensitivities")
    