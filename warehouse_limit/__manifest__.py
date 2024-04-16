{
    'name': 'Warehouse Limit',
    'depends': ['stock','sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/sale_order_line_views.xml',
        'views/stock_move_views.xml',
        'wizards/quantity_limit.xml'
    ]
}