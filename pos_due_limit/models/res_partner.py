# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.company,
        help='Company which conducts the auction')
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        default=lambda self: self.env.company.currency_id.id)
    due_limit = fields.Monetary('Due Limit')
    due_amount = fields.Integer('Due Amount', compute='_compute_due_amount',store=True)


    def _compute_due_amount(self):
        for rec in self:
            invoiced_amount = rec.env['pos.order'].search([
                ('partner_id', '=', rec.id),
                # ('move_type', '=', 'out_invoice'),
                ('state', 'in', ['invoiced'])
            ]).mapped('amount_total')
            print(invoiced_amount)
            rec.due_amount = sum(invoiced_amount)
            print(rec.due_amount)

