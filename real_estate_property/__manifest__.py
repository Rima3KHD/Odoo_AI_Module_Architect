{
    'name': 'Real Estate Property',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties',
    'description': """Module for managing real estate properties, including listings, types, and offers.""",
    'author': 'Your Name',
    'website': '',
    'license': 'LGPL-3',
    'depends': ["base", "web"],
    'data': [
        'security/ir.model.access.csv',
        
        'views/real_estate_property_views.xml',
        
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}