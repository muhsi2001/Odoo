from odoo import http
from odoo.http import request

class BidEnd(http.Controller):
   @http.route(['/bid-end'], type='http', auth="user", website=True)
   def bid_end(self):
      print('aa')
      values= {}
      return request.render("fleet_auction.bid_thankyou_form", values)
