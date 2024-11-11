{
    'name': 'AMBIENTA Customizations',

    'version': '1.0',

    'summary': 'Customizations for AMBIENTA',

    'category': 'Sales',

    'author': 'ST/Am',

    'website': '',
    'depends': ['sale', 'mrp'],
    'data': [
        'data/paperformat_cotizador.xml',
        'report/sale_order_report_template.xml',
        'report/sale_order_report.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/res_user_view.xml',
        'views/res_config.xml',       
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
