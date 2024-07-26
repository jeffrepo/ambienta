{
    'name': 'AMBIENTA Customizations',

    'version': '1.0',

    'summary': 'Customizations for AMBIENTA',

    'category': 'Sales',

    'author': 'ST/Am',

    'website': '',
    'depends': ['sale', 'mrp'],
    'data': [
        'report/sale_order_report_template.xml',
        'report/sale_order_report.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
