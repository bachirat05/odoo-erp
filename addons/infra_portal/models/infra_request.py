from odoo import models, fields

class InfraRequest(models.Model):
    _name = 'infra.request'
    _description = 'Demande Web d\'Infrastructure'

    name = fields.Char(string='Sujet de la demande', required=True)
    type = fields.Selection([
        ('access', 'Demande d\'accès (Nouvelle VM)'),
        ('issue', 'Signalement de problème (Serveur/VM)')
    ], string='Type de demande', required=True)
    
    description = fields.Text(string='Description détaillée', required=True)
    
    state = fields.Selection([
        ('draft', 'Nouvelle'),
        ('in_progress', 'En cours'),
        ('done', 'Traitée')
    ], string='État', default='draft')

    user_id = fields.Many2one('res.users', string='Demandeur', default=lambda self: self.env.user)
    
    # Liaisons avec le module core
    server_id = fields.Many2one('infra.server', string='Serveur concerné')
    vm_id = fields.Many2one('infra.vm', string='VM concernée')