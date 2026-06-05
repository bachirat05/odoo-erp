{
    'name': 'Infra Software & Licences',
    'version': '1.0',
    'summary': 'Gestion des licences logicielles et alertes',
    'category': 'IT Management',
    'depends': ['base', 'infra_core'], 
    'data': [
        'security/ir.model.access.csv',
        'views/licence_views.xml',
    ],
    'installable': True,
    'application': False,
}