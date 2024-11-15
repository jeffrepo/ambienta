from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    labor_product_id = fields.Many2one(
        'product.product',
        string="Producto de Mano de Obra")
    