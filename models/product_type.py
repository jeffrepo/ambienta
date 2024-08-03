from odoo import models, fields

class ProductType(models.Model):
    _name = 'product.type'
    _description = 'Product Type'

    name = fields.Char(string="Nombre")
    price = fields.Float(string="Precio")
