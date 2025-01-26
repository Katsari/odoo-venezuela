from odoo import api, fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    client_city_id = fields.Many2one("res.country.city", string="Customer city")
    state_customer_id = fields.Many2one("res.country.state", string="Customer state")

    @api.model
    def _select(self):
        res = super()._select()
        res += """,
            move.client_city_id as client_city_id,
            move.state_customer_id as state_customer_id
        """
        return res
