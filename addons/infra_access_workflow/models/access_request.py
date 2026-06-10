from odoo import models, fields, api
from datetime import date

class InfraAccessRequest(models.Model):
    _name = 'infra.access.request'
    _description = 'Demande de Ressource Informatique'

    name = fields.Char(string='Référence', required=True, copy=False, default='Nouveau')
    requester_id = fields.Many2one('res.users', string='Demandeur', required=True, default=lambda self: self.env.user)
    project = fields.Char(string='Projet', required=True)
    vm_id = fields.Many2one('infra.vm', string='VM demandée')
    server_id = fields.Many2one('infra.server', string='Serveur demandé')
    date_start = fields.Date(string='Date de début', required=True, default=fields.Date.today)
    date_end = fields.Date(string='Date de fin prévue')
    duration_days = fields.Integer(string='Durée (jours)', compute='_compute_duration', store=True)
    reason = fields.Text(string='Justification')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('pending', 'En attente de validation DSI'),
        ('allocated', 'Alloué'),
        ('returned', 'Rendu'),
    ], string='État', default='draft', tracking=True)
    notes = fields.Text(string='Notes DSI')

    @api.depends('date_start', 'date_end')
    def _compute_duration(self):
        for rec in self:
            if rec.date_start and rec.date_end:
                delta = rec.date_end - rec.date_start
                rec.duration_days = delta.days
            else:
                rec.duration_days = 0

    def action_submit(self):
        for rec in self:
            rec.state = 'pending'

    def action_allocate(self):
        for rec in self:
            rec.state = 'allocated'
            if rec.vm_id:
                rec.vm_id.state = 'allocated'

    def action_return(self):
        for rec in self:
            rec.state = 'returned'
            if rec.vm_id:
                rec.vm_id.state = 'stopped'

    def action_reset_draft(self):
        for rec in self:
            rec.state = 'draft'
