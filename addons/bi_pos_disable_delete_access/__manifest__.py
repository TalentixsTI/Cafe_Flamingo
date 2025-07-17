# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Delete Access Disable in POS',
    'version': '18.1',
    'category': 'Point of Sale',
    'summary': 'POS access rights pos delete button disable pos delete access disable delete access in pos delete access disable on point of sales access rights pos restrict delete order restriction pos delete order restriction pos access control pos hide delete button',
    'description': """

        Disable POS Access Odoo App helps users to restrict the deletion based on the access rights. User can enable or disable delete access rights from user configuration. If user has true access of disable delete, They will not have a delete option in the POS order otherwise delete option available to that user.
    
    """,
    'author': 'BrowseInfo',
    "price": 15,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.com/demo-request?app=bi_pos_disable_delete_access&version=17&edition=Community',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/res_user_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'bi_pos_disable_delete_access/static/src/xml/TicketScreen.xml',
        ],
    },
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'live_test_url': 'https://www.browseinfo.com/demo-request?app=bi_pos_disable_delete_access&version=17&edition=Community',
    "images": ['static/description/Disable-Delete-Access-in-POS-Banner.gif'],
}
