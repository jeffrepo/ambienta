from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    show_price = fields.Boolean(string="Show Price")
 

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.create_manufacturing_orders()
        return res

    def create_manufacturing_orders(self):
        for order in self:
            for line in order.order_line:
                if line.product_id.bom_ids:
                    for bom in line.product_id.bom_ids:
                        mo = self.env['mrp.production'].create({
                            'product_id': line.product_id.id,
                            'product_qty': line.product_uom_qty,
                            'product_uom_id': line.product_uom.id,
                            'origin': order.name,
                            'bom_id': bom.id,
                        })
                        mo.action_confirm()
                        self.update_manufactured_product_price(mo)

    def update_manufactured_product_price(self, mo):
        total_sale_price = sum([line.product_id.lst_price for line in mo.bom_id.bom_line_ids])
        mo.product_id.write({'lst_price': total_sale_price})
