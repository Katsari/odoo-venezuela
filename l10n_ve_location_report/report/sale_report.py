from odoo import models, fields, api


class SaleReportCityClient(models.Model):
    _inherit = "sale.report"

    client_city_id = fields.Many2one("res.country.city", string="Customer city")
    state_customer_id = fields.Many2one("res.country.state", string="Customer state")

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["client_city_id"] = "s.client_city_id"
        res["state_customer_id"] = "s.state_customer_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            s.client_city_id,
            s.state_customer_id
            """
        return res
