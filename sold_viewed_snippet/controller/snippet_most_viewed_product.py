from odoo import http
from odoo.http import request


class ViewedProducts(http.Controller):

   @http.route('/most_viewed_products', type='json', auth="public")
   def most_viewed_products(self):
      view= request.env['website.visitor'].sudo().search([])
      b= view.sorted('visitor_product_count', reverse=True)

      prod= b.mapped('product_ids')
      print(prod)
      values = []
      for rec in prod:
         values.append({
            'name': rec.name,
            'website': rec.website_url,
            'image': rec.image_1920
         })
      viewed_prod = [values[i:i+4] for i in range(0, len(values), 4)]
      print('kk', len(viewed_prod[0]))
      return viewed_prod
