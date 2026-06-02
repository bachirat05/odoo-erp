from odoo import models, fields

class InfraIP(models.Model):
    _name = 'infra.ip'
    _description = 'Adresse IP'

    name = fields.Char(string='Adresse IP', required=True)
    vm_id = fields.Many2one('infra.vm', string='VM associée')
    type = fields.Selection([('public', 'Publique'), ('private', 'Privée')], string='Type')
    _sql_constraints = [
    ('unique_ip', 'unique(name)', 'Cette adresse IP existe déjà!')
    ]