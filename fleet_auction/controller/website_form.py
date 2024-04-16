from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):

   @http.route('/fleetauction', type='http', auth="user", website=True)
   def show_auction(self):
       ongoing_bids = (request.env['fleet.auction'].
                       search([('state', '=', 'ongoing')]))
       draft_bids = (request.env['fleet.auction'].
                     search([('state', '=', 'draft')]))
       confirmed_bids = (request.env['fleet.auction'].
                         search([('state', '=', 'confirmed')]))
       cancelled_bids = (request.env['fleet.auction'].
                         search([('state', '=', 'cancelled')]))
       success_bids = (request.env['fleet.auction'].
                       search([('state', '=', 'success')]))
       values = {'ongoing': ongoing_bids,
                 'draft': draft_bids,
                 'confirmed': confirmed_bids,
                 'cancelled': cancelled_bids,
                 'success': success_bids}
       return request.render("fleet_auction.auction_view_form", values)
