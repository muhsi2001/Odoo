# Part of Odoo. See LICENSE file for full copyright and licensing details.

import hmac
import logging
import pprint

from werkzeug.exceptions import Forbidden

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request


_logger = logging.getLogger(__name__)


class PaytrailController(http.Controller):
    _return_url = '/payment/paytrail/return'

    @http.route(_return_url, type='http', methods=['GET'], auth='public')
    def paytrail_return_from_checkout(self, **data):
        print('mmm')
        """ Process the notification data sent by Paytrail after redirection
        from checkout.

        :param dict data: The notification data.
        """
        _logger.info("Handling redirection from Paytrail with data:\n%s",
                     pprint.pformat(data))
        # Handle the notification data.
        if data.get('checkout-status') != 'pending':

            (request.env['payment.transaction'].sudo()._handle_notification_data
             ('paytrail', data))
        else:  # The customer cancelled the payment by clicking
            # on the close button.
            pass  # Don't try to process this case because the
            # transaction id was not provided.

        # Redirect the user to the status page.
        return request.redirect('/payment/status')

