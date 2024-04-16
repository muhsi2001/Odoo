# -*- coding: utf-8 -*-

{
    'name': 'Fleet Auction',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Fleet Auction',
    'author': "Mike",
    'description': "Fleet Auction",
    'summary': "Manages fleet auction activities.",
    'depends': ['fleet', 'account', 'website', 'crm', 'product'],
    'data': [
        'security/auction_security.xml',
        'security/ir.model.access.csv',
        'report/auction_report.xml',
        'data/website_menu.xml',
        'data/report_paperformat_data.xml',
        'data/mail_template.xml',
        'data/auction_end_template.xml',
        'data/auction_sequence.xml',
        'data/start_and_end_date_cron.xml',
        'wizards/cancel_auction.xml',
        'wizards/auction_report_wizard_views.xml',
        'views/fleet_auction_views.xml',
        'views/auction_expense_view.xml',
        'views/auction_bid_views.xml',
        'views/fleet_vehicle_views.xml',
        'views/website_form_views.xml',
        'views/auction_details_form_view.xml',
        'views/bid_creation_form_view.xml',
        'views/bid_end_views.xml',
        'views/fleet_auction_menu.xml',
        'views/auction_bid_menu.xml',
        'report/ir_action_report_fleet_auction.xml',
    ],
    'installable': True,
    'application': True,
    'assets' : {
        'web.assets_backend': [
            'fleet_auction/static/src/js/action_manager.js',
            ],
    }
}
