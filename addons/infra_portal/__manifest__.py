{
    "name": "Infra Web Portal",
    "version": "1.0",
    "category": "Website",
    "summary": "Portail web pour les demandes d'accès et signalements IT",
    "author": "Fatima-Ezzahra Bellachheb",
    "depends": ["base", "website", "portal", "infra_core"],
    "data": [
        "security/ir.model.access.csv",
        "views/infra_request_views.xml",
        "views/portal_templates.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": False,
}