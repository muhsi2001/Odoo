from odoo import http
from odoo.http import request


class BidForm(http.Controller):
   @http.route('/bid', type='http', auth="user", website=True)
   def bid_creation(self):
      auctions = (request.env['fleet.auction'].
                  search([('state', '=', 'ongoing')]))
      customers = request.env['res.partner'].search([])
      values = {
         'customers': customers,
         'auctions': auctions
      }
      return request.render("fleet_auction.bid_creation_form", values)

   @http.route('/bid/submit/', type='http', auth="user", website=True)
   def create_auction_bid(self, **kw):
      request.env['auction.bid'].sudo().create({
         'name': kw.get('name', False),
         'auction_id': kw.get('auction_id', False),
         'bid_price': kw.get('price', False),
         'bid_amt': kw.get('amount', False),
         'bid_date': kw.get('date', False),
         'customer': kw.get('partner_id', False)
      })
      return request.render('fleet_auction.bid_thankyou_form', {})
