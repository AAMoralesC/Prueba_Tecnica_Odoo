from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_accounting_admin = fields.Boolean(
        compute='_compute_is_accounting_admin',
        string='Es Admin de Contabilidad'
    )

    @api.depends_context('uid')
    def _compute_is_accounting_admin(self):
        is_admin = self.env.user.has_group('account.group_account_manager')
        for partner in self:
            partner.is_accounting_admin = is_admin

    @api.model
    def default_get(self, fields_list):
        res = super(ResPartner, self).default_get(fields_list)
        if 'property_payment_term_id' in fields_list:
            immediate_term = self.env.ref('account.account_payment_term_immediate', raise_if_not_found=False)
            if immediate_term:
                res['property_payment_term_id'] = immediate_term.id
        return res

    def write(self, vals):
        if 'property_payment_term_id' in vals:
            old_terms = {partner.id: partner.property_payment_term_id for partner in self}
            
            res = super(ResPartner, self).write(vals)
            
            now = fields.Datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_name = self.env.user.name
            
            for partner in self:
                old_term = old_terms.get(partner.id)
                new_term = partner.property_payment_term_id
                
                if old_term != new_term:
                    old_name = old_term.name if old_term else "Sin término"
                    new_name = new_term.name if new_term else "Sin término"
                    
                    message = f'[{now}] Usuario "{user_name}" cambió el Término de pago de "{old_name}" a "{new_name}".'
                    partner.message_post(body=message)
            return res
            
        return super(ResPartner, self).write(vals)
