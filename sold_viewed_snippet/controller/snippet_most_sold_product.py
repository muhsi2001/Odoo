from odoo import http
from odoo.http import request


class SoldProducts(http.Controller):

   @http.route('/most_sold_products', type='json', auth="public")
   def most_sold_products(self):
      sold  = request.env['product.template'].sudo().search([])
      a = sold.sorted('sales_count', reverse=True)
      print(a)
      values=[]
      for rec in a:
         values.append({
            'name': rec.name,
            'website': rec.website_url,
            'image': rec.image_1920
         })
      prod= [values[i:i+4] for i in range(0, len(values), 4)]
      return prod
