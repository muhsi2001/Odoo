SUPPORTED_CURRENCIES = [
    'GBP',
    'CAD',
    'XAF',
    'CLP',
    'COP',
    'EGP',
    'EUR',
    'GHS',
    'GNF',
    'KES',
    'MWK',
    'MAD',
    'NGN',
    'RWF',
    'SLL',
    'STD',
    'ZAR',
    'TZS',
    'UGX',
    'USD',
    'XOF',
    'ZMW',
]

# Mapping of transaction states to Flutterwave payment statuses.
PAYMENT_STATUS_MAPPING = {
    'pending': ['pending auth'],
    'done': ['successful'],
    'cancel': ['cancelled'],
    'error': ['failed'],
}

# The codes of the payment methods to activate when Flutterwave is activated.
DEFAULT_PAYMENT_METHODS_CODES = [
    # Primary payment methods.
    'card',
    'mpesa',
    # Brand payment methods.
    'visa',
    'mastercard',
    'amex',
    'discover',
]

PAYMENT_METHODS_MAPPING = {
    'bank_transfer': 'banktransfer',
}
