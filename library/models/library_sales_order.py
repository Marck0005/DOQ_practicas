from odoo import models, fields, api, _
from odoo.exceptions import UserError

class LibrarySalesOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):       
        if self.partner_id.is_partner:
            res = super(LibrarySalesOrder, self).action_confirm()

            self.with_delay().generate_invoice(self.id)

            return res
        else:
            raise UserError(_("You can only sell to partners"))
        

    
    
    @api.model
    def generate_invoice(self, sale_order_id):
        # Método que se ejecutará en el job para generar la factura
        sale_order = self.env['sale.order'].browse(sale_order_id)

        # Genera la factura utilizando la API pública
        invoices = self.env['account.move'].create({
            'partner_id': sale_order.partner_id.id,
            'type': 'out_invoice',  # Tipo de factura de venta
            'invoice_date': fields.Date.today(),
        })

        # Asocia las líneas del pedido de venta a la factura
        for line in sale_order.order_line:
            self.env['account.move.line'].create({
                'move_id': invoices.id,
                'product_id': line.product_id.id,
                'quantity': line.product_uom_qty,
                'price_unit': line.price_unit,
                'account_id': line.product_id.property_account_income_id.id,
            })

        # Registra el pago automáticamente (opcional)
        invoices.action_post()

        return True

        