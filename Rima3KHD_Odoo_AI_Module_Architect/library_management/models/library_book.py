from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'A book in the library'

    
    name = fields.Char("Title", required=True)
    
    author_id = fields.Many2one("Author")
    
    isbn = fields.Char("ISBN")
    
    date_published = fields.Date("Publication Date")
    
    active = fields.Boolean("Active")
    