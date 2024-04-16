# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
   _inherit = 'res.config.settings'

   product_location_id = fields.Many2one(
      related='pos_config_id.product_location_id',
      config_parameter='product_loc.product_location',
      readonly=False)
