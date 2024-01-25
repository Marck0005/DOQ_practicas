from odoo import models, fields, api


class LibraryAuditMixing(models.AbstractModel):
    _name = 'library.audit.mixing'
    
    
    
    @api.model
    def create(self, vals):
        # create the book record
        record = super(LibraryAuditMixing, self).create(vals)

        # create an audit line
        self.env['library.audit'].create({
            'operation': 'create',
            'record_id': record.id,
            'record_model': self._name,
            'date': fields.Datetime.now(),
        })

        return record
    
    

    def write(self, vals):
        res = super(LibraryAuditMixing, self).write(vals)
        for record in self:
            self.env['library.audit'].create({
                'operation': 'write',
                'record_id': record.id,
                'record_model': record._name,
                'date': fields.Datetime.now(),
            })
        return res
    
 
    def unlink(self):
        for record in self:
            self.env['library.audit'].create({
                'operation': 'unlink',
                'record_id': record.id,
                'record_model': record._name,
                'date': fields.Datetime.now(),
            })
        res = super(LibraryAuditMixing, self).unlink()
        return res

    
