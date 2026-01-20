{
    'name': 'Real Estate',
    'version': '18.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties and offers',
    'description': """This module allows you to manage real estate properties, their details, and associated purchase offers.""",
    'author': 'Your Company',
    'website': '',
    'license': 'LGPL-3',
    'depends': ["base", "web"],
    'data': [
        'security/ir.model.access.csv',
        
        'views/real_estate_property_views.xml',
        
        'views/property_offer_views.xml',
        
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}