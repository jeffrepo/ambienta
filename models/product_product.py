from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    labor_product_id = fields.Many2one(
        'product.product',
        string="Producto de Mano de Obra")
