from odoo import models, fields, api, _
from datetime import timedelta



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
    
    
    
    
    # x x x x x H x D 
    
    @api.model
    def send_mail_notice(self):
        recordset = self.search([('state', '=', 'pending'), ('devolution_date' , '<=', fields.Datetime.now() + timedelta(days=self.env.company.days))])
        for rec in recordset:
            ctx = {}
            ctx['email_to'] = rec.partner_id.email
            ctx['partner_name'] = rec.partner_id.name
            ctx['email_from'] = self.env.user.email
            ctx['send_email'] = True
            template = self.env.ref('library.book_rent_mail_template')
            template.with_context(ctx).send_mail(rec.id, force_send=True , raise_exception=False)
    
    
    def launch_wizard_mail_notice(self):
        self.ensure_one()
        template_id = self.env.ref('library.book_rent_mail_template').id
        ctx ={
            'default_model': 'library.book.rent',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.partner_id.email,
            'partner_name': self.partner_id.name,
            'email_from': self.env.user.email,
            }      
                
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
        