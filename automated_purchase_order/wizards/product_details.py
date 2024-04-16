# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductDetails(models.TransientModel):
    _name = 'product.details'

    product_id = fields.Many2one(
        comodel_name='product.template', string='Product',
        help='Name of the corresponding product')
    variant_id = fields.Many2one(
        'product.product', string='Variant',
        domain="[('product_tmpl_id', '=' , product_id)]",
        help='Variants of the corresponding product')
    # available_variants=fields.Many2many('product.product')
    quantity = fields.Integer('Quantity', help='Quantity of the product')
    price = fields.Float('Price', help='Price of the product')
    vendor_id = fields.Many2one(
        comodel_name='res.partner', string='Vendor',
        help='Vendor inside the product chosen')
    date = fields.Date.today()

    def create_rfq_po_bill(self):
        """function defined to create rfq,po,receipt
        and bill on a single button click"""
        for vendor in self.product_id.seller_ids:
            existing_rfq = self.env['purchase.order'].search([
                ('partner_id', '=', vendor.partner_id[0].id),
                ('state', 'in', ['draft']),
            ])

            if existing_rfq:
                existing_rfq.write({
                    'order_line':[fields.Command.create({
                        'product_id': self.variant_id.id,
                        'product_qty': self.quantity,
                        'price_unit': self.price
                })]
                })
                existing_rfq.button_confirm()
            else:
                rfq = self.env['purchase.order'].create({
                    'partner_id': vendor.partner_id[0].id,
                    'order_line': [(fields.Command.create({
                        'product_id': self.variant_id.id,
                        'product_qty': self.quantity,
                        'price_unit': self.price
                    })
                    )]
                })
                rfq.button_confirm()

                for picking in rfq.picking_ids:
                    picking.button_validate()

                rfq.action_create_invoice()
                self.env['account.move'].search(
                    [('state', '=', 'draft')]).write({
                        'state': "posted",
                        'invoice_date': self.date,
                    })
