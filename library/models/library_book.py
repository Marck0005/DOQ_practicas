from odoo import fields, models


class LibraryBooks(models.Model):
    _name = 'library.book'
    _description = 'Model for book registry'
    
    _inherits = {'product.template': 'product_tmpl_id'}
     

    #Campo que relaciona el libro creado con un objeto de tipo product
  
    product_tmpl_id = fields.Many2one(
        string='product_tmpl_id',
        comodel_name='product.template',
        ondelete='cascade',
        auto_join = True,
        required = True,
    )
  
    
    #Relación con autores, como un autor puede tener muchos libros pero 
    # un libro solo tiene un autor es many2one (muchos libros tienen solo 1 autor)
    author_id = fields.Many2one(comodel_name='res.partner', string='')
    
    #Relación con generos, como un libro puede tener muchos generos y un genero puede tener muchos
    #libros es many2many 
    genre_ids = fields.Many2many(comodel_name='library.book.genre')
    
    
    
    
    #Edicion --> Int
    edition = fields.Integer(string='Edition' )
    
    #Impreso o digital --> Selección
    book_type = fields.Selection(string='Book type', selection=[('printed', 'Printed'), ('digital', 'Digital'),])
    
    #Enlace web de compra --> Caracteres
    web = fields.Char(string='Purchase Link')
    
    #Se ha comprado --> Bool
    is_purchased = fields.Boolean(string='Is purchased?')
    
    #Fecha de compra --> DateTime
    date = fields.Datetime(string='Date Purchase')
    
    
    
