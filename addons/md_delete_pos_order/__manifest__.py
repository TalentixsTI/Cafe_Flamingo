# -*- coding: utf-8 -*-
# Powered by Mindphin.
# © 2023 Mindphin. (<https://www.mindphin.com>).

{
    "name": "Delete POS Order",
    "author": "Mindphin",
    'website': "https://www.mindphin.com",
    "license": "OPL-1",
    'support': 'info@mindphin.com',
    "version": "18.0.1.0",
    "category": "Point of Sale",
    "summary":
    """ The 'Delete POS Order' Module In Odoo Empowers Users To Efficiently Manage Paid POS Orders Offering Flexibility Through Configurable Security Options Users Can Seamlessly Delete Single Or Multiple Orders Enhancing Overall Point Of Sale Transaction Control
    Delete POS order | Cancel transaction | Remove order | delete pos order | delete order | pos configuration | POS Order Delete | delete records | delete session.
    """,
    "description":
        """The innovative "POS Order Deletion" Module Is A Game Changer In Simplifying The Process Of Removing Paid Or Posted Point Of Sale Orders Within The Odoo Platform By Providing Users With The Choice Between Delete POS Order Without Code And Delete POS Order With Code Options This Module Offers Unparalleled Flexibility Allowing Users To Efficiently Manage And Delete Single Or MultipleOrders According To Their Specific Needs And Preferences Ultimately Enhancing Their Overall Workflow And Productivity
        """,
    "depends": ['base', 'point_of_sale'],
    "data": [
        'security/ir.model.access.csv',
        'security/pos_delete_paid_order.xml',
        'views/res_users.xml',
        'wizard/delete_order_wiz.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 20,
    'currency': 'USD',
}
