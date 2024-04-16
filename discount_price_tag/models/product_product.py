# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    is_discounted_product = fields.Boolean(
        string='Discounted Product',
        help='To show whether the product is a discounted product or not')
