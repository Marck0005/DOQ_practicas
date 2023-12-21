from odoo import models, fields, api

class LibraryAudit(models.Model):
    _name = 'library.audit'
    _description = 'Library Audit'




    operation = fields.Selection(string='',
                                 selection=[('create', 'Create'),
                                            ('write', 'Write'),
                                            ('unlink', 'Unlink')])
    
    user_id = fields.Many2one(comodel_name='res.users',
                              string='User',)
    
    book_id = fields.Many2one(comodel_name='library.book',string='Book')
    
    
    
    date = fields.Datetime(
        string='',
        default=fields.Datetime.now,
    )
    
    
    
    
    
    
    
    # Add more fields as needed

    # Add methods and other class definitions here
