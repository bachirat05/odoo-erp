from odoo import models, fields, api

class InfraServerStat(models.Model):
    _name = 'infra.server.stat'
    _description = 'Statistique par serveur'
    _auto = False  # vue SQL, pas une vraie table

    name = fields.Char(string='Serveur')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('in_use', 'En utilisation'),
        ('maintenance', 'En maintenance'),
    ], string='État')
    vm_count = fields.Integer(string='Nombre de VMs')
    ram = fields.Integer(string='RAM (Go)')
    cpu = fields.Integer(string='CPUs')

    def init(self):
        """Crée une vue SQL pour alimenter les graphiques Odoo."""
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW infra_server_stat AS (
                SELECT
                    s.id          AS id,
                    s.name        AS name,
                    s.state       AS state,
                    s.ram         AS ram,
                    s.cpu         AS cpu,
                    COUNT(v.id)   AS vm_count
                FROM infra_server s
                LEFT JOIN infra_vm v ON v.server_id = s.id
                GROUP BY s.id, s.name, s.state, s.ram, s.cpu
            )
        """)