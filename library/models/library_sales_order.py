from odoo import models, fields, api
from odoo.exceptions import UserError

class LibrarySalesOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):       
        if self.partner_id.is_partner == True:
            res = super(LibrarySalesOrder, self).action_confirm()
            return res
        else:
            raise UserError("You can only sell to partners") 
