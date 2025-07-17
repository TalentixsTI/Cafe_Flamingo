{
    'name': 'Facturación electrónica Costa Rica POS',
    'version': '1.0',
    'author': 'Odoo CR, TechMicro Inc S.A.',
    'license': 'OPL-1',
    'website': 'http://www.techmicrocr.com',
    'category': 'Account',
    'description':
    '''
    Facturación electronica POS Costa Rica.
    ''',
    'depends': [
        'factura_electronica_cr',
        'point_of_sale'
    ],
    'data': [
        'views/electronic_invoice_views.xml',
        'data/data.xml',
        'data/payment_methods_data.xml',
        'views/pos_payment_method.xml'
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'cr_electronic_invoice_pos/static/src/**/*',
        ],
    },
    'installable': True,
}
