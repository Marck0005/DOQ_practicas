from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _name = "res.config.settings"
    _inherit = "res.config.settings"

    days = fields.Integer(string="Days before notice", related="company_id.days", readonly=False)