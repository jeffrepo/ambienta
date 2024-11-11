import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    type_id = fields.Many2one('product.type', string="Tipo")
    show_quotation = fields.Boolean(string="Mostrar Cotización")
    show_price = fields.Boolean(string="Mostrar Precio")
    page_break = fields.Boolean(string="Salto de Página")

    @api.onchange('type_id')
    def _onchange_type_id(self):
        if self.type_id:
            self.price_unit += self.type_id.price


    @api.model
    def create(self, vals):
        # Crear la línea original del pedido
        order_line = super(SaleOrderLine, self).create(vals)
        _logger.info("Línea de pedido creada: %s", order_line)

        # Obtener el producto configurado como mano de obra desde la configuración
        labor_product_id = self.env['ir.config_parameter'].sudo().get_param('sale.labor_product_id')
        _logger.info("Producto de mano de obra obtenido de la configuración: %s", labor_product_id)

        # Solo proceder si el producto no es el de mano de obra y la línea es un producto (display_type is None)
        if labor_product_id and int(labor_product_id) != order_line.product_id.id and not order_line.display_type:
            # Crear una línea de pedido adicional para el producto de mano de obra justo después de la línea de pedido original
            labor_line = self.create({
                'order_id': order_line.order_id.id,
                'product_id': int(labor_product_id),
                'product_uom_qty': 1,
                'price_unit': self.env['product.product'].browse(int(labor_product_id)).lst_price,
                'sequence': order_line.sequence + 1  # Colocar la línea inmediatamente después del producto original
            })
            _logger.info("Línea de mano de obra creada justo después del producto: %s", labor_line)
        else:
            _logger.info("No se añadió la línea de mano de obra porque el producto es el mismo configurado en labor_product_id o la línea no es un producto.")

        return order_line