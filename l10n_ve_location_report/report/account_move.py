from odoo import models, api, fields


class AccountMove(models.Model):

    _inherit = "account.move"

    client_city_id = fields.Many2one(
        related="partner_id.city_id", string="Customer city", store=True
    )

    state_customer_id = fields.Many2one(
        related="partner_id.state_id", string="Customer state", store=True
    )


