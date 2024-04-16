{
    'name': 'Product Available Quantity',
    'depends': ['point_of_sale','product'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/product_product_views.xml',
    ],
    'assets': {
            'point_of_sale._assets_pos':[
                '/product_available_quantity/static/src/xml/product_card.xml',
                '/product_available_quantity/static/src/xml/product_widget.xml',
            ]
        }
}