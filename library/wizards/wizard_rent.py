from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class WizardRent(models.TransientModel):
    _name = 'wizard.rent'
    _description = 'Transient model for rent books'
    
    #Many2one porque muchos alquileres pueden tener el mismo partner
    partner_id = fields.Many2one('res.partner', string='Partner', domain=[('is_partner', '=', True)] ,required = True)
    
    #Many2one porque muchos alquileres pueden tener el mismo libro
    book_id = fields.Many2one('library.book', string='Book',required = True)
    
    rent_date = fields.Datetime(string='Rent date', default = fields.Datetime.now(),required = True)
    devolution_date = fields.Datetime(string='Devolution date', default=lambda self: (self.rent_date or fields.Datetime.now()) + timedelta(weeks=3),required = True)    
    
 
    def rent(self):
    # Count the number of rented books for the partner
        #partners = self.env['res.partner'].search([('is_partner', '=', True)])
        rented_books_count = self.env['library.book.rent'].search_count([
        ('partner_id', '=', self.partner_id.id),
        ('state', '=', 'pending')
    ])

    # Check if the partner has more than 2 rented books
        if rented_books_count >= 2:
            raise ValidationError(_("This partner has already rented 2 or more books."))
        else:
        # Rent the book
            self.env['library.book.rent'].create({
            'partner_id': self.partner_id.id,
            'book_id': self.book_id.id,
            'rent_date': self.rent_date,
            'devolution_date': self.devolution_date,
            'state': 'pending'
        })