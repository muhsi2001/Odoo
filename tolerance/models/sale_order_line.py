# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    tolerance = fields.Float(string='Tolerance',
                             related='order_partner_id.tolerance',
                             readonly=False)
