from odoo import models,fields


class  SaleInherit(models.Model):

    _inherit = 'sale.order'

    date_sale = fields.Date(string='Sale Date')

