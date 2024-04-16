{
    'name': 'Tolerance',
    'version': '17.0.1.0.0',
    'category': 'Marketing/Tolerance',
    'author': "Mike",
    'description': "Tolerance",
    'summary': "Tolerance",
    'depends': ['base','contacts','sale','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/sale_order_line.xml',
        'views/purchase_order_line.xml',
        'views/stock_move.xml',
        'views/sale_order_views.xml',
        'wizards/tolerance_wizard.xml'
        ]
}