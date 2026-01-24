{
    'name': 'Beauty Salon Management',
    'version': '18.0.1.0.0',
    'category': 'Services',
    'summary': 'Manage beauty salon appointments, services, and clients',
    'description': """A comprehensive system for managing a beauty salon. It handles client information, service catalog, staff management, appointment scheduling, and service history.""",
    'author': 'Odoo Community',
    'website': '',
    'license': 'LGPL-3',
    'depends': ["base", "web", "calendar"],
    'data': [
        'security/ir.model.access.csv',
        
        'views/beauty_salon_client_views.xml',
        
        'views/beauty_salon_service_views.xml',
        
        'views/beauty_salon_staff_views.xml',
        
        'views/beauty_salon_appointment_views.xml',
        
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}