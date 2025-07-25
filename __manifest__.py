{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Sistema de gestión de biblioteca',
    'author': 'Mike',
    'category': 'Library',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/menu_views.xml',
        'views/member_views.xml',
        'views/book_views.xml',
        'views/loan_views.xml', 

    ],
    'assets': {
        'web.assets_backend': [
       
            # aquí podrás añadir CSS/JS en el futuro
        ],
    },
    'installable': True,
    'application': True,
}
