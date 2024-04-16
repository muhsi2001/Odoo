# -*- coding; utf-8 -*-

import hashlib
import hmac
import logging
import pprint
import json

import requests
from werkzeug.urls import url_join

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.payment_paytrail import const

_logger = logging.getLogger(__name__)


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('paytrail', "Paytrail")],
        ondelete={'paytrail': 'set default'}
    )
    paytrail_key_id = fields.Char(
        string="Paytrail Key Id",
        help="The key solely used to identify the account with Paytrail.",
        required_if_provider='paytrail',
    )
    paytrail_key_secret = fields.Char(
        string="Paytrail Key Secret",
        required_if_provider='paytrail',
        groups='base.group_system',
    )

    def _paytrail_make_request(self, endpoint, payload=None, method='POST'):
        """ Make a request to Paytrail API at the specified endpoint.

                Note: self.ensure_one()

                :param str endpoint: The endpoint to be reached by the request.
                :param dict payload: The payload of the request.
                :param str method: The HTTP method of the request.
                :return The JSON-formatted content of the response.
                :rtype: dict
                :raise ValidationError: If an HTTP error occurs.
                """

        self.ensure_one()

        url = url_join('https://services.paytrail.com', endpoint)
        headers = dict({"checkout-account": self.paytrail_key_id,
                        "checkout-algorithm": "sha256",
                        "checkout-method": 'POST',
                        "checkout-nonce": "564635208570152",
                        "checkout-timestamp": "2018-07-06T10:01:31.904Z",
                        "signature": self._paytrail_calculate_signature
                        (data=payload)})

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'

        try:
            if method == 'GET':
                response = requests.get(url, params=payload, headers=headers,
                                        timeout=10)
            else:
                response = requests.post(url, json=payload, headers=headers,
                                         timeout=10)
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                _logger.exception(
                    "Invalid API request at %s with data:\n%s",
                    url, pprint.pformat(payload),
                )
                raise ValidationError("Paytrail: " + _(
                    "The communication with the API failed. "
                    "Paytrail gave us the following "
                    "information: '%s'", response.json().get('message', '')
                ))
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            _logger.exception("Unable to reach endpoint at %s", url)
            raise ValidationError(
                "Paytrail: " + _("Could not establish the connection to the API.")
            )
        return response.json()

    def _paytrail_calculate_signature(self, data):
        """ Compute the signature for the request's
        data according to the Razorpay documentation.
        :return: The calculated signature.
        :rtype: str
        """
        headers = dict({"checkout-account": self.paytrail_key_id,
                        "checkout-algorithm": "sha256",
                        "checkout-method": 'POST',
                        "checkout-nonce": "564635208570152",
                        "checkout-timestamp": "2018-07-06T10:01:31.904Z"})

        class Crypto:

            # /
            # @param message Raw string
            # @param secret Merchant shared secret
            # @return
            # /
            @staticmethod
            def compute_sha256_hash(message: str, secret: str) -> str:

                # whitespaces that were created during json parsing process must be removed
                hash = hmac.new(secret.encode(), message.encode(),
                                digestmod=hashlib.sha256)
                return hash.hexdigest()

            # /
            # @param secret Merchant shared secret
            # @param headerParams Headers or query string parameters
            # @param body Request body or empty string for GET request
            # @return
            # /
            @staticmethod
            def calculate_hmac(self, secret: str, headerParams: dict,
                               body: str = '') -> str:

                data = []
                for key, value in headerParams.items():
                    if key.startswith('checkout-'):
                        data.append(
                            '{key}:{value}'.format(key=key, value=value))

                data.append(body)
                return self.compute_sha256_hash('\n'.join(data), secret)

        body_dump = json.dumps(data)
        s = self.paytrail_key_secret
        encData = Crypto.calculate_hmac(Crypto, s, headers, body_dump)
        return encData
