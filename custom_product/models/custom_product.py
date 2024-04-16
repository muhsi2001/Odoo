# -*- coding: utf-8 -*-

from odoo import fields, models


class CustomProduct(models.Model):
    _name = 'custom.product'

    product_id = fields.Many2one(comodel_name='product.template')

