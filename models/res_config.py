from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    labor_product_id = fields.Many2one('product.product', string='Mano de obra', config_parameter='sale.labor_product_id')
