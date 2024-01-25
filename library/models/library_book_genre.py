from odoo import fields, models

class LibraryBookGenre(models.Model):
    _name = 'library.book.genre'
    _description = 'Model for book genre registry'
    _inherit = 'library.audit.mixing'

    
    name = fields.Char(string='')
    
    
