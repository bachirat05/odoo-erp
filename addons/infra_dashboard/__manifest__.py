{
    'name': 'Infra Dashboard & Analytics',
    'version': '1.0',
    'summary': 'Tableaux de bord et analyse des ressources IT',
    'description': """
        Module de visualisation et d'analyse pour l'infrastructure IT.
        - Taux d'utilisation des serveurs et VMs
        - Statistiques RAM / CPU / Stockage
        - Graphiques et tableaux croisés dynamiques
    """,
    'author': 'Amadjouj Manar',
    'category': 'Technical',
    'depends': ['base', 'infra_core',  ], # modèles infra.server, infra.vm, infra.cluster, infra.ip
    'data': [
        'security/ir.model.access.csv',
        'views/infra_dashboard_views.xml',
        'views/infra_server_stat_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}