# -- coding: utf-8 --
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sub Project Management',
    'version': '18.0.0.0',
    'category': 'Project',
    'summary': 'Project Subproject management project sub project management task subtask task sub task sub project task subtask sub project with sub project under project under subproject project planning project task planning sub project planning',
    'description': """ 

        Allow Users to Manage Sub Projects of Project on odoo,
        Sub Project Management in odoo,
        Project Sub Project in odoo,
        Manage Sub Projects in odoo,
        Set Project Co-Ordinator Rule in odoo,
        Divide Projects and Sub Projects in odoo,
        Display Warning on Deletion of Project and Sub Project in odoo,

    
    """,
    'author': 'BrowseInfo',
    "price": 25,
    'license': 'OPL-1',
    "currency": 'EUR',
    'website': 'https://www.browseinfo.in',
    'depends': ['base', 'project'],
    'data': [
        'security/sub_project_security.xml',
        'security/ir.model.access.csv',
        'views/sub_project_view.xml',
        'views/project_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'live_test_url': 'https://youtu.be/9a-hp5AYICg',
    "images": ['static/description/Banner.png'],
}
