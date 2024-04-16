

from odoo import fields, models


class AuctionExpenses(models.Model):
    _name = "auction.expenses"
    _description = "Auction Expenses"

    expense_ids = fields.Many2one('fleet.auction')
    exp_product_id = fields.Many2one(
        string='Expense Product', comodel_name='product.product',
        help='Services created during the auction')
    description = fields.Char(
        string='Description', related='exp_product_id.name',
        help='Description about the service product')
    sub_total_price = fields.Float(
        string='Sub Total', related="exp_product_id.list_price", readonly=False,
        help='Price of the product')
