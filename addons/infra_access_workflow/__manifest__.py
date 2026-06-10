{
    "name": "Infra Access Workflow",
    "version": "1.0",
    "category": "IT Infrastructure",
    "summary": "Gestion des demandes de ressources et workflow de validation",
    "author": "Membre C",
    "depends": ["base", "infra_core"],
    "data": [
        "security/ir.model.access.csv",
        "views/access_request_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": False,
}
