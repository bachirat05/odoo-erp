from odoo import http
from odoo.http import request

class InfraWebPortalController(http.Controller):

    @http.route(['/infra/support'], type='http', auth='user', website=True)
    def infra_support_page(self, **kw):
        servers = request.env['infra.server'].sudo().search([])
        vms = request.env['infra.vm'].sudo().search([])
        
        # On utilise "infra_portal" ici
        return request.render('infra_portal.template_infra_support', {
            'servers': servers,
            'vms': vms,
        })

    @http.route(['/infra/support/submit'], type='http', auth='user', website=True, methods=['POST'])
    def infra_support_submit(self, **post):
        request.env['infra.request'].sudo().create({
            'name': post.get('name'),
            'type': post.get('type'),
            'description': post.get('description'),
            'server_id': int(post.get('server_id')) if post.get('server_id') else False,
            'vm_id': int(post.get('vm_id')) if post.get('vm_id') else False,
            'user_id': request.env.user.id,
        })
        
        # Et on utilise "infra_portal" ici aussi
        return request.render('infra_portal.template_infra_success', {})