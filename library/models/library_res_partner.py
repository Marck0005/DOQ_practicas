from odoo import  fields, models, api

class LibraryResPartner(models.Model):
    
    _name = 'library.book.author'
    _inherits = {'res.partner': 'author_id'}

    author_id= fields.Many2one(
        'res.partner', 
        string='Author', 

     )
    
    
    
    first_name = fields.Char(string='')
    
    last_name = fields.Char(string='')

    name = fields.Char(compute = '_compute_name', store = True)
    
    

    book_ids = fields.One2many(
        'library.book', 
        'author_id', 
        string='Books'
    )
    
    genres_ids = fields.Many2many(comodel_name='library.book.genre')
    

    
    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            name = ''
            if rec.first_name:
                name += rec.first_name
            if rec.last_name:
                name += ' ' + rec.last_name
            rec.name = name.strip()
        

    

    
class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    is_partner = fields.Boolean(string='Partner')
    partner_number = fields.Integer(string='')

    