# -*- coding: utf-8 -*-

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    tolerance = fields.Float(string='Tolerance',
                             related='partner_id.tolerance', readonly=False)
