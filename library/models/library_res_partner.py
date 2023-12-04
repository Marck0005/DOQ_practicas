from odoo import  fields, models

class LibraryResPartner(models.Model):
    
    _name = 'library.book.author'
    _inherits = {'res.partner': 'author_id'}

    author_id= fields.Many2one(
        'res.partner', 
        string='Author', 

     )

    
    

    book_ids = fields.One2many(
        'library.book', 
        'author_id', 
        string='Books'
    )
    
    genres_ids = fields.Many2many(comodel_name='library.book.genre')

    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    is_partner = fields.Boolean(string='Partner')
    partner_number = fields.Integer(string='')

    