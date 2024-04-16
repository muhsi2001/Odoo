{
    'name': 'Payment Paytrail',
    'depends': ['payment','website','account','base'],
    'data':[
        'views/payment_paytrail_template.xml',
        'views/payment_provider_views.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml',
        'data/payment_invoice_data.xml'
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}