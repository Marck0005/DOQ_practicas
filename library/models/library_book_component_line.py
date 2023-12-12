from odoo import fields, models, api

class LibraryBookComponentLine(models.Model):
    _name = 'library.book.component.line'
    _description = 'Model for book genre registry'
    
    #Un pack tiene muchos componentes
    pack_id = fields.Many2one(comodel_name='library.book')
    #name = fields.Char(related='component_ids.name' , readonly=False)
    book_quantity = fields.Integer(string='')
    component_id = fields.Many2one(comodel_name='library.book')
    
    
    
