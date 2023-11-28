from odoo import  fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_partner = fields.Boolean(string = 'Partner')
    is_author = fields.Boolean(string = 'Author')
    
    
    partner_number = fields.Integer(string = '')
    
    #respartner rescompany resuser
    

    
