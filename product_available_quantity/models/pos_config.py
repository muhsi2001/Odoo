# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    product_location_id = fields.Many2one(
        string='Product Location',
        comodel_name='stock.location',
        help='Field for choosing different locations in warehouse')
