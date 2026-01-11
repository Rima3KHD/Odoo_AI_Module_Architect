from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Book Author'

    
    name = fields.Char("Name", required=True)
    
    biography = fields.Text("Biography")
    