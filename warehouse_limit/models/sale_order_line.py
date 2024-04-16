# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_stock_limit = fields.Float(
        string='Limit', related='product_template_id.product_stock_limit',
        readonly=True)
