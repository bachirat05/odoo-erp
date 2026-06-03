from odoo import models, fields

class InfraServer(models.Model):
    _name = 'infra.server'
    _description = 'Serveur Physique'

    name = fields.Char(string='Nom du serveur', required=True)
    ram = fields.Integer(string='RAM (Go)')
    cpu = fields.Integer(string='Nombre de CPUs')
    storage = fields.Integer(string='Stockage (Go)')
    os = fields.Char(string='Système d\'exploitation')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('in_use', 'En utilisation'),
        ('maintenance', 'En maintenance'),
    ], default='available', string='État')
    vm_ids = fields.One2many('infra.vm', 'server_id', string='VMs hébergées')