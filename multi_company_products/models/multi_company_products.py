# -*- coding: utf-8 -*-

from odoo import models


class MultiCompanyProducts(models.Model):
    _name = "multi.company.products"
    _description = "multi company products"

    # def button_validate(self):
    #
    #     records = self.move_ids_without_package
    #     print("button")
    #
    #     for record in records:
    #         max_range = record.product_uom_qty + record.tolerance
    #         min_range = record.product_uom_qty - record.tolerance
    #
    #         if not min_range <= record.quantity <= max_range:
    #
    #             if record.quantity < min_range:
    #                 if not self.accept:
    #                     self.write({'accept': True})
    #                     return {'name': 'Warning',
    #                             'type': 'ir.actions.act_window',
    #                             'res_model': 'tolerance.warning.wizard',
    #                             'view_mode': 'form',
    #                             'view_type': 'form',
    #                             'target': 'new'}
    #                 else:
    #                     self.write({'accept': False})
    #                     validate = super(StockPicking,
    #                                      self).button_validate()
    #                     return validate
    #             else:
    #                 print('a')
    #                 return {'name': 'Warning',
    #                         'type': 'ir.actions.act_window',
    #                         'res_model': 'tolerance.warning.wizard',
    #                         'view_mode': 'form',
    #                         'view_type': 'form',
    #                         'target': 'new'}
    #         else:
    #             validate = super(StockPicking,
    #                              self).button_validate()
    #             return validate
    #
    # def accept_transfer(self):
    #     print("accept_transfer")
    #     validate = super(StockPicking, self).button_validate()
    #     return validate



    # def button_validate(self):
        #     res = super(StockPicking, self).button_validate()
        #
        #     # Check for each move if the quantity falls out of the tolerance range
        #     for move in self.move_ids_without_package:
        #         if move.product_id and move.product_id.sale_line_id:
        #             sale_line = move.product_id.sale_line_id
        #             min_quantity = sale_line.product_uom_qty - sale_line.tolerance
        #             max_quantity = sale_line.product_uom_qty + sale_line.tolerance
        #
        #             if move.quantity_done < min_quantity or move.quantity_done > max_quantity:
        #                 # Open the wizard if the quantity is out of tolerance range
        #                 action = self.env.ref(
        #                     'your_module_name.action_sale_order_line_tolerance_wizard').read()[
        #                     0]
        #                 action['context'] = {
        #                     'default_accept_tolerance': False,
        #                     'default_move_id': move.id,
        #                 }
        #                 return action
        #
        #     return res