# -*- coding; utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_stock_limit = fields.Float(string="Product Stock Limit")
