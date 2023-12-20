from odoo import models, fields, api, _
from odoo.exceptions import UserError

class LibrarySalesOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):       
        if self.partner_id.is_partner:
            res = super(LibrarySalesOrder, self).action_confirm()
            return res
        else:
            raise UserError(_("You can only sell to partners"))