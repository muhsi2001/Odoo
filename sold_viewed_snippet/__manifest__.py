{
    'name': 'Sold Viewed Snippet',
    'depends': ['website','product'],
    'data': [
        'views/snippets/s_most_viewed_products.xml',
        'views/snippets/s_most_sold_products.xml',
    ],
    'assets': {
        'web.assets_frontend': [
                'sold_viewed_snippet/static/src/js/sold_snippet.js',
                'sold_viewed_snippet/static/src/xml/sold_products.xml',
                'sold_viewed_snippet/static/src/js/view_snippet.js',
                'sold_viewed_snippet/static/src/xml/view_products.xml',
        ]
    }
}