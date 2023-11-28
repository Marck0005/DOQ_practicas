from odoo import fields, models


class LibraryBooks(models.Model):
    _name = 'library.book'
    _description = 'Model for book registry'
    
    
    #Nombre Libro --> Caracteres
    name = fields.Char(string='Name', required=True)
    
    #Precio --> Float
    price = fields.Float(string='Price')
    
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
    
    
    
