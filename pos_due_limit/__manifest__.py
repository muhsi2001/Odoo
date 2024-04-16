{
    'name': 'POS Due Limit',
    'depends': ['contacts','point_of_sale'],
    'data': [
        'views/res_partner_views.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_due_limit/static/src/js/pos_validate.js',
            'pos_due_limit/static/src/xml/partner_details.xml',
        ]
    }
}