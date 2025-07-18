{
    'name': 'Facturación electrónica Costa Rica',
    'version': '18.0.1.0.0',
    'author': 'Odoo CR Community',
    'license': 'AGPL-3',
    'website': 'https://github.com/odoocr',
    'category': 'Accounting',
    'summary': 'Electronic Invoicing for Costa Rica',
    'description':
        '''
        Electronic invoicing solution for Costa Rica.
        ''',
    'depends': [
        'base',
        'product',
        'uom',
        'sale_management',
        'sales_team',
        'sale_stock',
        'account',
        'l10n_cr',
        'l10n_cr_country_codes',
        'l10n_cr_hacienda_info_query',
        'res_currency_cr_adapter',
    ],
    'data': [
        'data/account_tax_group_data.xml',
        'data/account_tax_template_data.xml',
        'data/aut_ex_data.xml',
        'data/code_type_product_data.xml',
        'data/identification_type_data.xml',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'data/payment_methods_data.xml',
        'data/reference_code_data.xml',
        'data/reference_document_data.xml',
        'data/sale_conditions_data.xml',
        'data/product_category_data.xml',
        'data/product_data.xml',
        'data/uom_data.xml',
        'data/economic_activity_data.xml',
        'data/sequence.xml',
        'data/res.currency.xml',
        'data/decimal_precision.xml',
        # 'data/account_tax_data.xml',
        'views/account_move_views.xml',
        'views/account_journal_views.xml',
        'views/account_payment_views.xml',
        'views/code_type_product_views.xml',
        'views/identification_type_views.xml',
        'views/product_views.xml',
        'views/reference_document_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/resolution_views.xml',
        'views/sale_condition_views.xml',
        'views/account_tax_views.xml',
        'views/economic_activity_views.xml',
        'views/menu_views.xml',
        'views/account_move_reversal_views.xml',
        'views/report_invoice_document.xml',
        'views/qr_code_invoice_view.xml',
        'views/account_portal_templates.xml',
        'security/ir.model.access.csv',
        
    ],
    'external_dependencies': {
        "python": [
            'cryptography',
            'xmlsig',
            'OpenSSL',
            'phonenumbers',
            'jsonschema',
        ],
    },
    'installable': True,
}