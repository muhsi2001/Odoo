from odoo import fields, models


class CancelAuction(models.TransientModel):
    _name = 'cancel.auction'

    cancel_reason = fields.Char(string='Cancel Reason',
                                help='The reason for cancelling the auction')

    def button_cancel(self):
        """Function defined to change the state to cancelled"""
        self.env['fleet.auction'].search([('state', '=', 'confirmed')]).write({
            'state': "cancelled"
        })
