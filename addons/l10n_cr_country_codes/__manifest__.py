{
    'name': 'Códigos País para Facturación electrónica Costa Rica',
    'version': '18.0.1.0.0',
    'author': 'Odoo CR',
    'license': 'AGPL-3',
    'website': 'https://github.com/odoocr',
    'category': 'Accounting',
    'summary': 'Códigos País para Facturación electrónica Costa Rica',
    'description': '''Códigos País para Facturación electrónica Costa Rica.''',
    'depends': [
        'base',
        'account',
        'product'
    ],
    'data': [
        'data/res_country_state.xml',
        'data/res.country.county.csv',
        'data/res.country.district.csv',
        'data/res.country.neighborhood.csv',
        'security/ir.model.access.csv',
        'views/country_codes_views.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
}
