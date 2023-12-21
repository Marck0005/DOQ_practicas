from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class LibraryBooks(models.Model):
    _name = 'library.book'
    _description = 'Model for book registry'
    _inherits = {'product.template': 'product_tmpl_id'}
     

    # Campo que relaciona el libro creado con un objeto de tipo product
  
    product_tmpl_id = fields.Many2one(
        string='product_tmpl_id',
        comodel_name='product.template',
        ondelete='cascade',
        auto_join=True,
        required=True,
    )
  
    
    #Relación con autores, como un autor puede tener muchos libros pero 
    # un libro solo tiene un autor es many2one (muchos libros tienen solo 1 autor)
    author_id = fields.Many2one(comodel_name='library.book.author', string='')
    
    #Relación con generos, como un libro puede tener muchos generos y un genero puede tener muchos
    #libros es many2many 
    genres_ids = fields.Many2many(comodel_name='library.book.genre')

    #Relación con componentes, como muchas lineas pueden pertenecer a un pack entonces one2many
    is_pack = fields.Boolean(string='')
    lines_ids = fields.One2many(comodel_name='library.book.component.line',
                                inverse_name='pack_id')
    

    #detailed_type = fields.Selection(related='product_tmpl_id.detailed_type')
    
    # Edicion --> Int
    edition = fields.Integer(string='Edition')
    
    pack_type = fields.Selection(string='Pack type',
                                 selection=[('saga', 'Saga'),
                                            ('collection', 'Collection')],
                                 default='collection')  # Set default value to 'collection'
    

    
    
    # Impreso o digital --> Selección
    book_type = fields.Selection(string='Book type',
                                 selection=[('printed', 'Printed'),
                                            ('digital', 'Digital'),])

# Enlace web de compra --> Caracteres
    web = fields.Char(string='Purchase Link')
    
    #Se ha comprado --> Bool
    is_purchased = fields.Boolean(string='Is purchased?')
    
    #Fecha de compra --> DateTime
    date = fields.Datetime(string='Date Purchase')
    
    #Si queremos usarlo en un constrain, hay que decrararlo en el modelo
    list_price = fields.Float(string='Price')
    
    
    @api.onchange('is_pack')
    def _onchange_is_pack(self):
        if self.is_pack == False:
            self.pack_type = False
            
    @api.onchange('author_id')
    def _onchange_genres_ids(self):
        self.genres_ids += self.author_id.genres_ids 
        
        
    @api.constrains('list_price')
    def _check_price(self):
        if self.list_price < 0:
            raise ValidationError(_("Price can't be less than 0"))
    
    
    
    @api.model
    def create(self, vals):
        # create the book record
        book = super(LibraryBooks, self).create(vals)

        # create an audit line
        self.env['library.audit'].create({
            'operation': 'create',
            'user_id': self.env.user.id,
            'book_id': book.id,
            'date': fields.Datetime.now(),
            # add other fields as necessary...
        })

        return book
    
    

    def write(self, vals):
        res = super(LibraryBooks, self).write(vals)
        for book in self:
            self.env['library.audit'].create({
                'operation': 'write',
                'user_id': self.env.user.id,
                'book_id': book.id,
                'date': fields.Datetime.now(),
            })
        return res
    
 
    def unlink(self):
        for book in self:
            self.env['library.audit'].create({
                'operation': 'unlink',
                'user_id': self.env.user.id,
                'book_id': book.id,
                'date': fields.Datetime.now(),
            })
        res = super(LibraryBooks, self).unlink()
        return res