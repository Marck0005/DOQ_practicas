from odoo import models, fields, api, _



class LibraryBookRent(models.Model):
    _name = 'library.book.rent'
    _description = 'Model for rent books'
    
    #Many2one porque muchos alquileres pueden tener el mismo partner
    partner_id = fields.Many2one('res.partner', string='Partner')
    
    #Many2one porque muchos alquileres pueden tener el mismo libro
    book_id = fields.Many2one('library.book', string='Book')
    
    rent_date = fields.Datetime(string='Rent date')
    devolution_date = fields.Datetime(string='Devolution date')
    real_devolution_date = fields.Datetime(string='Real devolution date')
    
    state = fields.Selection(string='State', selection = [('pending', 'Pending'), ('returned', 'Returned')])