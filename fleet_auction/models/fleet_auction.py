# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class FleetAuction(models.Model):
    _name = "fleet.auction"
    _description = "fleet auction"
    _inherit = 'mail.thread'
    _rec_name = "sequence_no"

    name = fields.Char(string='Name')
    vehicle_id = fields.Many2one(
        'fleet.vehicle.model', string="Vehicle Name",
        help='Name of the vehicle', related='')
    brand = fields.Char('Brand', help='Brand of the vehicle')
    responsible_id = fields.Many2one(
        'res.users', string='Responsible',
        default=lambda self: self.env.user,
        help='Person who is responsible for the auction')
    start_date = fields.Date(
        'Start Date', help='Starting date of the auction')
    end_date = fields.Date(
        'End Date', help='Ending date of the auction')
    date_today = fields.Date(string='Today Date',
                             default=lambda s: fields.Date.context_today(s))
    active = fields.Boolean(
        'Active', default=True,
        help='If active is set to false,'
             'the data will be archived')
    bid_count = fields.Integer(
        string='Bid Count', compute='_compute_bid_count')
    state = fields.Selection(
         string='State',
         tracking=True,
         default='draft',
         selection=[('draft', 'Draft'), ('confirmed', 'Confirmed'),
                    ('ongoing', 'Ongoing'), ('success', 'Success'),
                    ('cancelled', 'Cancelled')])
    description = fields.Html(
        'Description', help='Description about the auction')
    image = fields.Image('Image', help='Image of the auction')
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.company,
        help='Company which conducts the auction')
    currency_id = fields.Many2one(
        'res.currency',
        related='company_id.currency_id',
        default=lambda
        self: self.env.company.currency_id.
        id)
    start_price = fields.Monetary(
        'Start Price', copy=False,
        help='Price when the auction starts')

    won_price = fields.Monetary(
        'Won Price', copy=False,
        help='The price at which the vehicle is won')

    customer_id = fields.Many2one(
        'res.partner', 'Customer',
        help='Person participating in the auction')

    phone_id = fields.Char(
        string='Phone', related='customer_id.phone',
        readonly=False,
        help='Phone Number of the customer')

    email_id = fields.Char(
        string='Email', related='customer_id.email',
        readonly=False, help='Email address of the customer')

    tags = fields.Many2many(
        'crm.tag', string='Tags')

    bid = fields.One2many(
        'auction.bid', inverse_name='auction_id',
        compute='_compute_confirmed_bids')
    auc_expense_ids = fields.One2many(
        comodel_name='auction.expenses', inverse_name='expense_ids')

    total_price = fields.Float(
        string='Total', compute='_compute_total_price', store=True)
    invoice_created = fields.Boolean(string='Invoice Created', default=False)

    invoice_id = fields.Many2one(comodel_name='account.move', string='Invoice')
    is_invoice_paid = fields.Boolean(string="Invoice Paid",
                                     compute="_compute_is_invoice_paid",
                                     store=True)
    ribbon_color = fields.Char(string="Ribbon Color",
                               compute="_compute_ribbon_color", store=True)
    sequence_no = fields.Char(string="Sequence Number", copy=False,
                              readonly=False, index=True,
                              default=lambda self: 'New')

    @api.model
    def create(self, vals_list):
        print(vals_list)
        """sequence creation"""
        if vals_list.get('sequence_no', 'New') == 'New':
            vals_list['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'fleet.auction.code')
            result = super(FleetAuction, self).create(vals_list)
            return result

    def button_confirm(self):
        """Function defined to change state to confirmed""" 
        self.write({
            'state': "confirmed"
        })

    def button_end(self):
        """Function defined to change the state to success"""
        self.write({
            'state': "success"
        })

        sorted_bids = self.bid.sorted(key=lambda bid: bid.bid_amt, reverse=True)

        if sorted_bids:
            self.write({'customer_id': sorted_bids[0].customer,
                        'won_price': sorted_bids[0].bid_amt})

        template = (self.env.ref
                    ('fleet_auction.auction_end_email_template'))
        template.send_mail(self.id, force_send=True)

    def button_stop(self):
        """Function defined to change the state to success"""
        self.write({
            'state': "cancelled"
        })

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Function defined to check the validation of dates"""
        for auction in self:
            if auction.end_date and auction.start_date > auction.end_date:
                raise ValidationError((
                    'Auction start date must be smaller than end date.'
                ))

    def _compute_bid_count(self):
        """Function defined to count the bids of a particular auction"""
        for rec in self:
            rec.bid_count = (self.env['auction.bid'].search_count
                             ([('auction_id', '=', rec.id)]))

    def _compute_confirmed_bids(self):
        """Function defined to retrieve only confirmed bids to the auction"""
        for rec in self:
            rec.bid = (self.env['auction.bid'].search([
                        ('state', '=', 'confirmed'),
                        ('auction_id', '=', rec.id)
                    ]))

    def action_open_bids(self):
        """Function defined to return the
        views while opening the smart button"""
        return {
             'type': 'ir.actions.act_window',
             'name': 'Bids',
             'view_mode': 'tree,form',
             'res_model': 'auction.bid',
             'domain': [('auction_id', '=', self.id)],
             'target': 'current'
         }

    @api.depends('auc_expense_ids')
    def _compute_total_price(self):
        """Function defined to calculate the total expenses"""
        for rec in self:
            rec.total_price = sum(rec.auc_expense_ids.mapped('sub_total_price'))

    def create_invoice(self):
        """Function defined to create an invoice for the auction"""
        expense = self.auc_expense_ids.filtered(lambda x: x.sub_total_price > 0)
        invoice_data = {
            'partner_id': self.customer_id.id,
            'invoice_line_ids': [],
            'move_type': 'out_invoice',
            'auction_inv_id': self.id
        }

        for rec in expense:
            invoice_data['invoice_line_ids'].append((0, 0, {
                        'product_id': rec.exp_product_id.id,
                        'price_unit': rec.sub_total_price,
                    }))

        invoice = self.env['account.move'].create(invoice_data)

        self.write({
            'invoice_created': True
        })
        self.invoice_id = invoice.id

        return {
            'name': "Invoice",
            'view_mode': 'form',
            'view_id': self.env.ref('account.view_move_form').id,
            'view_type': 'form',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'type': 'ir.actions.act_window',
        }

    def action_show_invoice(self):
        """Shows invoice once the smart button is clicked"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.depends('invoice_id.payment_state')
    def _compute_is_invoice_paid(self):
        """Function checks whether the invoice is paid or not"""
        for auction in self:
            auction.is_invoice_paid = auction.invoice_id.payment_state == 'paid'

    @api.depends('is_invoice_paid')
    def _compute_ribbon_color(self):
        """Function defined to compute the ribbon color
        based on payment state"""
        for auction in self:
            auction.ribbon_color = 'green' if auction.is_invoice_paid else 'red'

    @api.model
    def start_and_end_auction(self):
        """Function defined to automatically move the auction
        state to ongoing based on the start date given"""
        today = fields.Date.today()
        self.search([('start_date', '=', today)]).write({
            'state': 'ongoing'
        })
        self.search([('end_date', '=', today)]).write({
            'state': 'success'
        })
