from odoo import models, fields, api


class InfraIncident(models.Model):
    """
    Signalement d'incident sur une ressource IT (VM ou Serveur).
    Créé depuis le portail web par n'importe quel utilisateur connecté.
    """
    _name = 'infra.incident'
    _description = 'Incident IT'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # ── Identification ────────────────────────────────────────────────
    name = fields.Char(
        string='Référence incident',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: 'Nouveau'
    )

    # ── Qui signale ───────────────────────────────────────────────────
    reporter_id = fields.Many2one(
        'res.partner',
        string='Signalé par',
        required=True,
        default=lambda self: self.env.user.partner_id
    )

    # ── Sur quelle ressource (modèles du Core) ────────────────────────
    resource_type = fields.Selection([
        ('vm', 'Machine Virtuelle'),
        ('server', 'Serveur Physique'),
    ], string='Type de ressource', required=True)

    vm_id = fields.Many2one(
        'infra.vm',
        string='VM concernée'
    )

    server_id = fields.Many2one(
        'infra.server',
        string='Serveur concerné'
    )

    # ── Détails de l'incident ─────────────────────────────────────────
    title = fields.Char(string='Titre de l\'incident', required=True)
    description = fields.Text(string='Description détaillée', required=True)

    priority = fields.Selection([
        ('0', 'Normale'),
        ('1', 'Urgente'),
        ('2', 'Critique'),
    ], default='0', string='Priorité')

    # ── Statut de traitement ──────────────────────────────────────────
    state = fields.Selection([
        ('new', 'Nouveau'),
        ('in_progress', 'En cours'),
        ('resolved', 'Résolu'),
        ('closed', 'Clôturé'),
    ], default='new', string='Statut', tracking=True)

    resolution_note = fields.Text(string='Note de résolution')

    # ── Séquence automatique ──────────────────────────────────────────
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Nouveau') == 'Nouveau':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'infra.incident'
                ) or 'Nouveau'
        return super().create(vals_list)

    # ── Nom affiché ───────────────────────────────────────────────────
    def _get_resource_name(self):
        """Retourne le nom de la ressource concernée"""
        self.ensure_one()
        if self.resource_type == 'vm' and self.vm_id:
            return self.vm_id.name
        elif self.resource_type == 'server' and self.server_id:
            return self.server_id.name
        return 'Non spécifié'
