from odoo import models, fields

class InfraCluster(models.Model):
    _name = 'infra.cluster'
    _description = 'Cluster'

    name = fields.Char(string='Nom du cluster', required=True)
    vm_ids = fields.One2many('infra.vm', 'cluster_id', string='VMs du cluster')