{
    'name': 'Discount Price Tag',
    'depends': ['product','point_of_sale'],
    'data': [
        'views/product_product_views.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos':[
            'discount_price_tag/static/src/js/pos_receipt.js',
            'discount_price_tag/static/src/xml/pos_receipt.xml',
            'discount_price_tag/static/src/xml/product_card.xml',
            'discount_price_tag/static/src/xml/product_widget.xml'
        ]
    }

}