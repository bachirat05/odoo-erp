{
    'name': 'Infra Dashboard & Analytics',
    'version': '1.0',
    'summary': 'Tableaux de bord et analyse budgétaire des ressources IT',
    'depends': ['base', 'infra_core'],  # dépend du module Core
    'data': [
        'security/ir.model.access.csv',
        'views/test.xml',  # ou ton fichier de vues principal
    ],
    'installable': True,
    'application': False,
}