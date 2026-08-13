from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_vat = fields.Char(
        string='RUT del Cliente',
        related='partner_id.vat',
        readonly=True,
        store=True,
    )
