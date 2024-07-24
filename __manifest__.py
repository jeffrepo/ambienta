{
    'name': 'AMBIENTA Customizations',

    'version': '1.0',

    'summary': 'Customizations for AMBIENTA',

    'category': 'Sales',

    'author': 'ST/Am',

    'website': '',
    'depends': ['sale', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
