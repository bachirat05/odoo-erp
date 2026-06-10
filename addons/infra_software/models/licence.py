from odoo import models, fields, api
from datetime import timedelta, date

class InfraLicence(models.Model):
    _name = 'infra.licence'
    _description = 'Licence Logicielle'

    # 1. Les champs basiques
    name = fields.Char(string="Nom du logiciel", required=True)
    license_key = fields.Char(string="Clé d'activation")
    cost = fields.Float(string="Coût (€)")
    expiration_date = fields.Date(string="Date d'expiration")
    
    # 2. Le lien avec le module A (La clé étrangère)
    server_id = fields.Many2one('infra.server', string="Installé sur le Serveur")

    # 3. Le système d'alerte (Champ calculé)
    is_expiring_soon = fields.Boolean(
        string="Expire dans moins de 30 jours", 
        compute="_compute_is_expiring_soon"
    )

    @api.depends('expiration_date')
    def _compute_is_expiring_soon(self):
        for record in self:
            if record.expiration_date:
                # Calcule la date limite (Aujourd'hui + 30 jours)
                limit_date = date.today() + timedelta(days=30)
                # Renvoie Vrai si la date d'expiration est avant ou égale à la date limite
                record.is_expiring_soon = record.expiration_date <= limit_date
            else:
                record.is_expiring_soon = False