# -*- coding: utf-8 -*-

{
    'name': 'Automated Purchase Order',
    'version': '17.0.1.0.0',
    'category': 'Marketing/Automated Purchase Order',
    'author': "Mike",
    'description': "Automated Purchase Order",
    'summary': "Manages Automation of Purchase Orders",
    'depends': ['purchase', 'account','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/automated_purchase_order_views.xml',
        'views/automated_purchase_order_menu.xml',
        'views/product_template_views.xml',
        'wizards/product_details.xml'
        ]
}