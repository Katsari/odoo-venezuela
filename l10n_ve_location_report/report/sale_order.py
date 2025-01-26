from odoo import fields, models, api


class SaleOrderLocation(models.Model):
    _inherit = "sale.order"

    client_city_id = fields.Many2one(
        related="partner_id.city_id", string="Customer city", store=True
    )

    state_customer_id = fields.Many2one(
        related="partner_id.state_id", string="Customer state", store=True
    )
