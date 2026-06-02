from odoo import models, fields, api


class InfraDashboard(models.Model):
    _name = 'infra.dashboard'
    _description = 'Tableau de bord Infrastructure IT'

    name = fields.Char(string='Nom du rapport', required=True)

    # ─── Statistiques Serveurs ───────────────────────────────────────────────

    total_servers = fields.Integer(
        string='Serveurs totaux',
        compute='_compute_server_stats',
        store=True,
    )
    servers_available = fields.Integer(
        string='Serveurs disponibles',
        compute='_compute_server_stats',
        store=True,
    )
    servers_in_use = fields.Integer(
        string='Serveurs en utilisation',
        compute='_compute_server_stats',
        store=True,
    )
    servers_maintenance = fields.Integer(
        string='Serveurs en maintenance',
        compute='_compute_server_stats',
        store=True,
    )
    server_usage_rate = fields.Float(
        string="Taux d'utilisation serveurs (%)",
        compute='_compute_server_stats',
        store=True,
        digits=(5, 2),
    )

    @api.depends()
    def _compute_server_stats(self):
        for rec in self:
            servers = self.env['infra.server'].search([])
            total = len(servers)
            in_use = len(servers.filtered(lambda s: s.state == 'in_use'))
            available = len(servers.filtered(lambda s: s.state == 'available'))
            maintenance = len(servers.filtered(lambda s: s.state == 'maintenance'))

            rec.total_servers = total
            rec.servers_in_use = in_use
            rec.servers_available = available
            rec.servers_maintenance = maintenance
            rec.server_usage_rate = (in_use / total * 100) if total > 0 else 0.0

    # ─── Statistiques VMs ────────────────────────────────────────────────────

    total_vms = fields.Integer(
        string='VMs totales',
        compute='_compute_vm_stats',
        store=True,
    )
    vms_running = fields.Integer(
        string='VMs en marche',
        compute='_compute_vm_stats',
        store=True,
    )
    vms_stopped = fields.Integer(
        string='VMs arrêtées (inutilisées)',
        compute='_compute_vm_stats',
        store=True,
    )
    vms_allocated = fields.Integer(
        string='VMs allouées',
        compute='_compute_vm_stats',
        store=True,
    )
    vm_usage_rate = fields.Float(
        string="Taux d'utilisation VMs (%)",
        compute='_compute_vm_stats',
        store=True,
        digits=(5, 2),
    )

    @api.depends()
    def _compute_vm_stats(self):
        for rec in self:
            vms = self.env['infra.vm'].search([])
            total = len(vms)
            running = len(vms.filtered(lambda v: v.state == 'running'))
            stopped = len(vms.filtered(lambda v: v.state == 'stopped'))
            allocated = len(vms.filtered(lambda v: v.state == 'allocated'))

            rec.total_vms = total
            rec.vms_running = running
            rec.vms_stopped = stopped
            rec.vms_allocated = allocated
            # VMs "actives" = running + allocated
            rec.vm_usage_rate = ((running + allocated) / total * 100) if total > 0 else 0.0

    # ─── Statistiques Ressources (RAM / CPU / Stockage) ─────────────────────

    total_ram = fields.Integer(
        string='RAM totale serveurs (Go)',
        compute='_compute_resource_stats',
        store=True,
    )
    total_cpu = fields.Integer(
        string='CPUs totaux serveurs',
        compute='_compute_resource_stats',
        store=True,
    )
    total_storage = fields.Integer(
        string='Stockage total serveurs (Go)',
        compute='_compute_resource_stats',
        store=True,
    )
    ram_allocated_vms = fields.Integer(
        string='RAM allouée aux VMs (Go)',
        compute='_compute_resource_stats',
        store=True,
    )
    cpu_allocated_vms = fields.Integer(
        string='vCPUs alloués aux VMs',
        compute='_compute_resource_stats',
        store=True,
    )

    @api.depends()
    def _compute_resource_stats(self):
        for rec in self:
            servers = self.env['infra.server'].search([])
            vms = self.env['infra.vm'].search([])

            rec.total_ram = sum(s.ram for s in servers)
            rec.total_cpu = sum(s.cpu for s in servers)
            rec.total_storage = sum(s.storage for s in servers)
            rec.ram_allocated_vms = sum(v.ram for v in vms)
            rec.cpu_allocated_vms = sum(v.cpu for v in vms)

    # ─── Statistiques Clusters ───────────────────────────────────────────────

    total_clusters = fields.Integer(
        string='Nombre de clusters',
        compute='_compute_cluster_stats',
        store=True,
    )
    avg_vms_per_cluster = fields.Float(
        string='VMs moyennes par cluster',
        compute='_compute_cluster_stats',
        store=True,
        digits=(5, 1),
    )

    @api.depends()
    def _compute_cluster_stats(self):
        for rec in self:
            clusters = self.env['infra.cluster'].search([])
            total = len(clusters)
            total_vms = sum(len(c.vm_ids) for c in clusters)

            rec.total_clusters = total
            rec.avg_vms_per_cluster = (total_vms / total) if total > 0 else 0.0

    # ─── Méthode de rafraîchissement manuel ──────────────────────────────────

    def action_refresh(self):
        """Recalcule toutes les statistiques à la demande."""
        self._compute_server_stats()
        self._compute_vm_stats()
        self._compute_resource_stats()
        self._compute_cluster_stats()
        return True


