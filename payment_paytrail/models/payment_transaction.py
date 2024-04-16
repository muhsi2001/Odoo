# -*- coding: utf-8 -*-

import logging

from werkzeug import urls

from odoo import _, models, fields
from odoo.exceptions import ValidationError

from odoo.addons.payment_paytrail.controller.main import PaytrailController
import random
import string

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return Paytrail-specific rendering values.

                Note: self.ensure_one() from `_get_processing_values`

                :param dict processing_values: The generic and specific
                processing values of the transaction
                :return: The dict of provider-specific processing values.
                :rtype: dict
                """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'paytrail':
            return res
            # Initiate the payment and retrieve the payment link data.

        base_url = self.provider_id.get_base_url()
        num = random.randint(100000, 999999)
        alpha = ''.join(random.choices(string.ascii_lowercase, k=10))
        payload = {
            'stamp': alpha + '-' + str(num) + '-',
            'reference': self.reference,
            'amount': self._calculate_amount(),
            'currency': 'EUR',
            'language': 'EN',
             "customer": {
                             "email": self.partner_email,
                              "firstName": self.partner_id.name,
                              "phone": self.partner_id.phone
             },
             "redirectUrls": {
                                "success": urls.url_join(base_url,PaytrailController._return_url),
                                "cancel": urls.url_join(base_url,PaytrailController._return_url)},
             }

        payment_link_data = self.provider_id._paytrail_make_request('payments',
                                                                    payload=payload)
        rendering_values = {'api_url': payment_link_data['href']}
        return rendering_values

    def _calculate_amount(self):
        euro = self.env['res.currency'].search([('name', '=', 'EUR')])

        if not euro:
            raise ValidationError(
                "paytrail: " + _("Currency Euro is not active"))
        else:
            if self.currency_id.name == 'USD':
                amount = (euro.rate_ids[0].inverse_company_rate * self.amount)*100
            else:
                usd_amount = (self.currency_id.rate_ids[0].inverse_company_rate*
                              self.amount)
                amount = (euro.rate_ids.inverse_company_rate * usd_amount)*100
            return int(amount)

    def _get_tx_from_notification_data(self, provider_code, notification_data):
        print('1', notification_data)
        """ Override of payment to find the transaction based on Paytrail data.

                :param str provider_code: The code of the
                provider that handled the transaction.
                :param dict notification_data: The notification
                data sent by the provider.
                :return: The transaction if found.
                :rtype: recordset of `payment.transaction`
                :raise ValidationError: If inconsistent data were received.
                :raise ValidationError: If the data match no transaction.
                """

        tx = super()._get_tx_from_notification_data(provider_code,
                                                    notification_data)
        if provider_code != 'paytrail' or len(tx) == 1:
            return tx

        reference = notification_data.get('checkout-reference')
        if not reference:
            raise ValidationError(
                "paytrail: " + _("Received data with missing reference."))

        tx = self.search(
            [('reference', '=', reference), ('provider_code', '=', 'paytrail')])
        if not tx:
            raise ValidationError(
                "paytrail: " + _("No transaction found matching reference %s.",
                               reference))
        return tx

    def _process_notification_data(self, notification_data):
        print('2', notification_data)
        """ Override of payment to process the transaction based on Paytrail data.

                Note: self.ensure_one()

                :param dict notification_data: The notification
                data sent by the provider.
                :return: None
                :raise ValidationError: If inconsistent data were received.
                """

        self.ensure_one()

        super()._process_notification_data(notification_data)
        if self.provider_code != 'paytrail':
            return

        # Update the provider reference.
        self.provider_reference = notification_data.get('checkout-transaction-id')

        # Update payment method.
        self.payment_method_id = (self.env.ref
                                  ('payment_paytrail.payment_method_paytrail').id)

        # Update the payment state.
        payment_status = notification_data.get('checkout-status')
        if payment_status in ['pending', 'new', 'delayed']:
            self._set_pending()
        elif payment_status == 'ok':
            self._set_done()
            # self._generate_invoice()
        elif payment_status == 'fail':
            self._set_canceled()
        else:
            self._set_error(
                _("An error occurred during the processing of your payment (status %s). Please try "
                  "again."))