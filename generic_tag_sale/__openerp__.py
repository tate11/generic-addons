# -*- coding: utf-8 -*-
{
    'name': "Generic Tag (Sale)",

    'summary': """
        Generic tag integration with sale addon
    """,

    'author': "Management and Accounting Online",
    'website': "https://maao.com.ua",

    'category': 'Uncategorized',
    'version': '9.0.0.1.0',

    "depends": [
        "generic_tag",
        "sale",
    ],

    "data": [
        'data/generic_tag_model.xml',
        'views/sale_order_view.xml',
        'views/sale_order_line_view.xml',
        'views/tag_view.xml',
    ],
    "installable": True,
    "auto_install": True,
    'license': 'Other proprietary',
}