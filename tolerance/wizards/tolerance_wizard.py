# -*- coding: utf-8 -*-

from odoo import models


class ToleranceWizard(models.TransientModel):
    _name = 'tolerance.wizard'

    def accept_tolerance_button(self):
        """Function defined to change the state from ready to done"""
        self.env['stock.picking'].search([('state', '=', 'assigned')]).write({
            'state': "done"
            })
