from odoo import http
from odoo.http import request



class Products(http.Controller):

   @http.route('/products', type='json', auth="public")
   def products(self):
      prod  = request.env['product.template'].sudo().search_read([], ['name', 'list_price'], limit=4)
      return prod