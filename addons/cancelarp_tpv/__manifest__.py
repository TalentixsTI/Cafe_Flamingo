{
    'name': 'Cancelar y Eliminar Restringido en TPV',
    'version': '1.0',
    'summary': 'Restringe la opción de eliminar pedidos en el TPV para usuarios no administradores.',
    'category': 'Point of Sale',
    'author': 'Tu Nombre',
    'depends': ['point_of_sale'],
    'data': [
        'views/point_of_sale_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'cancelarp_tpv/static/src/xml/ControlButton/TakeAway.xml',
            'cancelarp_tpv/static/src/xml/ControlButton/ticket_screen.xml',
            'cancelarp_tpv/static/src/js/ticket_screen.js',
            'cancelarp_tpv/static/src/js/TakeAway.js',
            'cancelarp_tpv/static/src/js/test.js',
            'cancelarp_tpv/static/src/xml/ControlButton/pos_pop_up.xml',


        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
