# -*- coding: utf-8 -*-

from odoo import api, fields ,models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    # has_variant = fields.Boolean(string='Has Variant', compute='_compute_has_variants', store=True)

    # @api.depends('product_variant_ids')
    # def _compute_has_variants(self):
    #     for product in self:
    #         product.has_variant=bool(product.product_variant_ids)

    def action_open_wizard(self):
        """function defined to open the wizard on button click"""
        return {
            'name': 'Product Details',
            'view_mode': 'form',
            'res_model': 'product.details',
            'view_id': self.env.ref
            ('automated_purchase_order.product_details_form').id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            # 'product':self.id,
            'context': {
                'default_product_id': self.id,
                'default_price': self.list_price
            }
        }
