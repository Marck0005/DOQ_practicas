from odoo import models, fields, api

class LibraryAudit(models.Model):
    _name = 'library.audit'
    _description = 'Library Audit'


    operation = fields.Selection(string='',
                                 selection=[('create', 'Create'),
                                            ('write', 'Write'),
                                            ('unlink', 'Unlink')])
    
    record_id = fields.Integer(string='')
    record_name = fields.Char(string='', compute='_compute_record_name')
    record_model = fields.Char(string='')    
    
    
    date = fields.Datetime(
        string='',
        default=fields.Datetime.now,
    )
    
    @api.depends('record_model', 'record_id')
    def _compute_record_name(self):
        for record in self:
            name = self.env[record.record_model].browse(record.record_id).name
            if name:
                record.record_name = name
            else:
                record.record_name = 'Not defined'