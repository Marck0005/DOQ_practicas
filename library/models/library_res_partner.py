from odoo import  fields, models, api
from odoo.exceptions import ValidationError

class LibraryResPartner(models.Model):
    
    _name = 'library.book.author'
    _inherits = {'res.partner': 'author_id'}
    _inherit = 'library.audit.mixing'

    author_id= fields.Many2one(
        'res.partner', 
        string='Author', 
        required=True,
        ondelete='cascade'
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
    
    unrented_books_ids = fields.One2many('library.book', string='Unrented Books', compute='_compute_unrented_books')
    
    total_sold = fields.Float(string='', compute = '_compute_total_sold' , compute_sudo = True)
    
    #El campo es sales_count
    def _compute_total_sold(self):
        for record in self:
            author_books = self.env['library.book'].search([('author_id', '=', record.id)])
            author_books_price = author_books.mapped('list_price')
            author_books_count = author_books.mapped('sales_count')
            record.total_sold = sum([price * count for price, count in zip(author_books_price, author_books_count)])
            
    
    
    
    
    def _compute_unrented_books(self):
        for record in self:
            author_books = self.env['library.book'].search([('author_id', '=', record.id)])
            rented_books = self.env['library.book.rent'].search([('book_id', 'in', author_books.ids)])
            unrented_books = author_books - rented_books.mapped('book_id')
            record.unrented_books_ids = unrented_books.mapped('id') if unrented_books else False
    
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
    _name = 'res.partner'
    _inherit = ['res.partner', 'library.audit.mixing']

    
    is_partner = fields.Boolean(string='Partner')
    partner_number = fields.Char(string='' , readonly = True, copy = False)
    name = fields.Char(string='', required=True, compute = '_compute_name', store = True, inverse='_inverse_name')
        
    #Numero de libros alquilados
    rented_book_number = fields.Integer(string='Rented Book Number', compute = '_compute_rents')
    
    #Recordset de los alquileres
    rent_ids = fields.One2many('library.book.rent', compute='_compute_rents')
    
    first_name = fields.Char(string='First Name')
    second_name = fields.Char(string='Second Name')
    
        
    def _inverse_name(self):
        for rec in self:
            if rec.name:
                names = rec.name.split(' ')
                rec.first_name = names[0]
                rec.second_name = ' '.join(names[1:]) if len(names) > 1 else ''
            else:
                rec.first_name = ''
                rec.second_name = ''


    @api.depends('first_name', 'second_name')
    def _compute_name(self):
        for rec in self:
            name = ''
            if rec.first_name:
                name += rec.first_name
            if rec.second_name:
                name += ' ' + rec.second_name
            rec.name = name.strip()
    
    def _compute_rents(self):
        #Desde la perspectiva de library.book.rent, agrupamos por partner_id y contamos los registros
        number = self.env['library.book.rent'].read_group([("partner_id", "=", self.id )], ['partner_id'], ['partner_id']) 
        self.rented_book_number = number[0]['partner_id_count'] if number else 0
        self.rent_ids = self.env['library.book.rent'].search([('partner_id', '=', self.id)])
        
    
    @api.model
    def create(self, vals):
        if vals.get('is_bookstore_partner', True):
            sequence = self.env['ir.sequence']
            vals['partner_number'] = sequence.next_by_code('res.partner') or '/'

        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if vals.get('is_bookstore_partner', True):
            sequence = self.env['ir.sequence']
            vals['partner_number'] = sequence.next_by_code('res.partner') or '/'

        return super(ResPartner, self).write(vals)
    
    def launch_wizard_unsubscribe(self):
        return {
            'name': 'Unsubscribe Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.unsubscribe',
            'view_mode': 'form',
            'target': 'new',
        }

    

    
    

