# -*- coding: utf-8 -*-

from odoo import fields ,models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    tolerance = fields.Float(string='Tolerance', compute='_compute_purchase_tolerance')

    def _compute_purchase_tolerance(self):
        order_line_tolerance = self.order_id._get_sale_orders().order_line
        for rec in order_line_tolerance:
            self.write({'tolerance': rec.tolerance})
            break
