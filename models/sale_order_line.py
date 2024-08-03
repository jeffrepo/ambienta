from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    type_id = fields.Many2one('product.type', string="Tipo")
    show_quotation = fields.Boolean(string="Show Quotation")

    @api.onchange('type_id')
    def _onchange_type_id(self):
        if self.type_id:
            self.price_unit += self.type_id.price
