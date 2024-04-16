# -*- coding: utf-8 -*-

{
    'name': 'Custom Product',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Custom Product',
    'author': "Mike",
    'description': "Custom Product",
    # 'summary': "Manages fleet auction activities.",
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_product_views.xml',
        'views/custom_product_menu.xml',
    ]
}