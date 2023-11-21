from odoo import fields, models


class LibraryBooks(models.Model):
    _name = 'library.book'
    _description = 'Model for book registry'
    
    
    #Nombre Libro --> Caracteres
    name = fields.Char(string='Name', required=True ,translate = True)
    
    #Precio --> Float
    price = fields.Float(string='Price')
    
    #Edicion --> Int
    edition = fields.Integer(string='Edition' ,translate = True)
    
    #Impreso o digital --> Selección
    book_type = fields.Selection(string='Book type', selection=[('printed', 'Printed'), ('digital', 'Digital'),], translate = True)
    
    #Enlace web de compra --> Caracteres
    web = fields.Char(string='Purchase Link',translate = True)
    
    #Se ha comprado --> Bool
    is_purchased = fields.Boolean(string='Is purchased?',translate = True)
    
    #Fecha de compra --> DateTime
    date = fields.Datetime(string='Date Purchase',translate = True)
    
