# -*- coding: utf-8 -*-

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        """function defined to pop up a warning when the onhand qty of
        product is less than the limit"""
        move = self.move_ids_without_package
        if not self._context.get('quantity_limit', False):

            for rec in move:
                qty_limit = rec.limit
                qty_available = rec.product_id.qty_available
                print('aa', qty_limit)
                print('bb', qty_available)

                if qty_available < qty_limit:
                    return {'name': 'Warning',
                            'type': 'ir.actions.act_window',
                            'res_model': 'quantity.limit',
                            'view_mode': 'form',
                            'view_type': 'form',
                            'target': 'new'}
        result = super(StockPicking, self).button_validate()
        return result
