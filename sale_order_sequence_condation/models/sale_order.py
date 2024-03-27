from odoo import api, fields, models, _
#
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    is_product = fields.Boolean(string="Is Product") 
    
    
    @api.model
    def create(self, vals):
        if vals.get("is_product") == True :
            vals['name'] = self.env['ir.sequence'].next_by_code('freight.order') or _("New")

        return super(SaleOrder, self).create(vals)
