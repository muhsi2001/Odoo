# -*- coding: utf-8 -*-

from odoo import fields, models


class AuctionBid(models.Model):
    _name = "auction.bid"
    _description = "Auction Bid"

    name = fields.Char('Name', help='Name of the bid')
    auction_id = fields.Many2one(
        'fleet.auction', string='Auction', ondelete='cascade',
        help='Specific auction in which this bid is happening.')
    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.company,
        help='Company which conducts the auction')
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        default=lambda self: self.env.company.currency_id.id)
    bid_price = fields.Monetary(
        'Bid Price', help='Price when the auction starts')
    bid_amt = fields.Monetary(
        'Bid Amount', help='Price when the auction starts')
    bid_date = fields.Date(
        string="Bid Date", help='Date at which auction is happening')
    customer = fields.Many2one(
        'res.partner', 'Customer',
        help='Person participating in the auction')
    phone_id = fields.Char(
        string='Phone', related='customer.phone',
        readonly=False, help='Phone Number of the customer')
    state = fields.Selection(
        string='State',
        tracking=True,
        default='confirmed',
        selection=[('draft', 'Draft'), ('confirmed', 'Confirmed')])

    def button_confirmed(self):
        """Function defined to change the state from draft to confirmed"""
        self.write({
            'state': 'confirmed'
        })

    def _compute_confirmed_bid(self):
        for rec in self:
            rec.confirmed_bids = self.search([
                ('state', '=', 'confirmed')
            ])
