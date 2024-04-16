# -*- coding; utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
   _inherit = 'product.product'

   available_qty = fields.Integer(
      'Available Quantity',
      compute='_compute_product_available_qty')

   def _compute_product_available_qty(self):
      """function defined for calculating
       product quantity based on location chosen in pos settings"""
      for rec in self:
         rec.available_qty = 0
         location = rec.env['ir.config_parameter'].sudo().get_param(
            'product_loc.product_location')
         products = rec.env['stock.quant'].search(
            [('location_id', '=', int(location)),
             ('product_id', '=', rec.id)])
         rec.available_qty = sum(products.mapped('quantity'))
