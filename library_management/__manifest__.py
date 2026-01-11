{
    'name': 'Library Management',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Manage books and authors',
    'description': """A comprehensive module to track library inventory, authors, and lending.""",
    'author': 'Antigravity',
    'website': '',
    'license': 'LGPL-3',
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        
        'views/library_book_views.xml',
        
        'views/library_author_views.xml',
        
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,
}