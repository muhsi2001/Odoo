# -*- coding: utf-8 -*-

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    limit = fields.Float(
        string='Limit',
        related='product_id.product_stock_limit', readonly=False)
