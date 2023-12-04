from odoo import fields, models, api

class LibraryBookGenre(models.Model):
    _name = 'library.book.genre'
    _description = 'Model for book genre registry'
    
    name = fields.Char(string='')
    
    
