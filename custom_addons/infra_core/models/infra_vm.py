from odoo import models, fields

class InfraVM(models.Model):
    _name = 'infra.vm'
    _description = 'Machine Virtuelle'

    name = fields.Char(string='Nom de la VM', required=True)
    ram = fields.Integer(string='RAM allouée (Go)')
    cpu = fields.Integer(string='vCPUs')
    storage = fields.Integer(string='Stockage (Go)')
    os = fields.Char(string='OS')
    server_id = fields.Many2one('infra.server', string='Serveur hôte')
    cluster_id = fields.Many2one('infra.cluster', string='Cluster')
    ip_ids = fields.One2many('infra.ip', 'vm_id', string='Adresses IP')
    state = fields.Selection([
        ('running', 'En marche'),
        ('stopped', 'Arrêtée'),
        ('allocated', 'Allouée'),
    ], default='stopped', string='État')