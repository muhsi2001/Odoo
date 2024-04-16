from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    auction_inv_id = fields.Many2one(
        comodel_name='fleet.auction',
        string='Auction Invoice',
        help='When invoice is created,the value is passed onto this field')

    def send_email_to_customer(self):
        mail_template = (self.env.ref
                         ('fleet_auction.auction_invoice_email_template'))
        mail_template.send_mail(self.auction_inv_id.id, force_send=True)
        print(self.auction_inv_id.id)

    def action_post(self):
        result = super(AccountMove, self).action_post()
        self.send_email_to_customer()
        # self.auction_inv_id.check()
        return result
