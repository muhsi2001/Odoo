{
    'name': 'Custom Snippet',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_product_views.xml',
        'views/demo_product_menu.xml',
        'views/snippets/s_custom.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_snippet/static/src/js/dynamic_snippet.js',
            'custom_snippet/static/src/xml/dynamic_snippet.xml',
        ]
    }
}