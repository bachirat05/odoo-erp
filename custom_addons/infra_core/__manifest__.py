{
    "name": "Infrastructure Core",
    "version": "1.0",
    "category": "IT Infrastructure",
    "summary": "Gestion des serveurs, VM, clusters et IP",
    "author": "Bachirat Salma",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/menus.xml",
        "views/infra_server_views.xml",
        "views/infra_vm_views.xml",
    ],
    "installable": True,
    "application": True,
}