# -*- coding: utf-8 -*-

from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = "fleet.vehicle"
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.company,
        help='Company which conducts the auction')
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        default=lambda
        self: self.env.company.currency_id.id)
    current_value = fields.Monetary(
        'Current Value', copy=False,
        help='Current Value of the vehicle')

    def open_auction_form(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Auction',
            'view_mode': 'form',
            'res_model': 'fleet.auction',
            'view_id': self.env.ref('fleet_auction.fleet_auction_form').id,
            'context': {
                'default_vehicle_id': self.model_id.id,
                'default_start_price': self.current_value,
            }
        }
