from odoo import http
from odoo.http import request


class AuctionDetailsForm(http.Controller):
   @http.route(['/auction/<int:rec_id>/'], type='http', auth="user",
               website=True)
   def auction(self, rec_id):
      data = request.env['fleet.auction'].sudo().browse(rec_id)
      values = {
         'data': data
      }
      return request.render("fleet_auction.auction_details_form", values)
