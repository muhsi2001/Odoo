# -*- coding: utf-8 -*-

from odoo import models


class QuantityLimit(models.TransientModel):
    _name = 'quantity.limit'

    def accept_transfer(self):
        """function defined to validate the transfer"""
        transfer_id = self._context.get('active_id')
        print(transfer_id)

        transfer = self.env['stock.picking'].browse(transfer_id)

        transfer.with_context(quantity_limit=True).button_validate()
