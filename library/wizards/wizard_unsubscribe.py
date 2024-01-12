from odoo import fields, models

class WizardUnsubscribe(models.TransientModel):
    _name = 'wizard.unsubscribe'
    _description = 'Model for unsubscribe partners'
    
    reason = fields.Text(string='Reason', required = True)

    def unsubscribe(self):
        partner_id = self._context["active_id"]
        entry = self.env["res.partner"].browse(partner_id)
        entry.write({"is_partner": False})
        entry.message_post(body=self.reason)