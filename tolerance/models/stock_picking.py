# -*- coding: utf-8 -*-

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        """Function defined to open a warning wizard while validating the
         transfer if quantity is greater or lesser than the range given"""
        result = super(StockPicking, self).button_validate()

        move = self.move_ids_without_package

        for rec in move:
            min_range = rec.product_uom_qty - rec.tolerance
            max_range = rec.product_uom_qty + rec.tolerance
            print(min_range)
            print(max_range)

            if not min_range <= rec.quantity <= max_range:
                return {'name': 'Warning',
                        'type': 'ir.actions.act_window',
                        'res_model': 'tolerance.wizard',
                        'view_mode': 'form',
                        'view_type': 'form',
                        'target': 'new'}
        return result
