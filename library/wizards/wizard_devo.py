from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class WizardDevo(models.TransientModel):
    _name = 'wizard.devo'
    _description = 'Transient model for devo books'
    
    partner_id = fields.Many2one('res.partner', string='Partner')
    book_id = fields.Many2one('library.book', string='Book' , domain = lambda self: [('id', 'in', self.env['library.book.rent'].search([('state', '=', 'pending')]).mapped('book_id.id'))])


    @api.onchange('book_id')
    def _onchange_book_id(self):
        partner_ids = self.env['library.book.rent'].search([('book_id', '=', self.book_id.id),('state', '=', 'pending')]).mapped('partner_id.id')
        
        return {'domain': {'partner_id': [('id', 'in', partner_ids)]}}

            

    def devo(self):
        record = self.env['library.book.rent'].search([
            ('partner_id', '=', self.partner_id.id),
            ('book_id', '=', self.book_id.id),
            ('state', '=', 'pending')
        ])      
        if len(record) == 1:
            values = {
                'real_devolution_date' : fields.Datetime.now(),
                'state' : 'returned'
            }
            record.write(values) 
        else:
            raise ValidationError(_("This partner has not rented this book."))
        