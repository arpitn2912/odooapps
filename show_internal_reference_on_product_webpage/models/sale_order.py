from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    type_of_service = fields.Selection(
        selection=[
            ('air', "Air"),
            ('land', "Land"),
            ('ocaen', "Ocean"),
         
        ],
        string="Status",
        default='air')
    
    
    domain1= fields.Char("Domain", compute='_compute_partner_invoice_id')    
    product_id = fields.Many2one("product.template", "Product")
    
    #domain="[('id', 'in', alternate_ids)]"
    
    
    
    
    @api.depends('type_of_service')
    def _compute_partner_invoice_id(self):
        for order in self:
            if order.type_of_service == "air":
                order.domain1 = [('sale_ok', '=', True)]
            elif order.type_of_service == "land":
                order.domain1 = [('sale_ok', '=', False)]
            elif order.type_of_service == "ocaen":
                order.domain1 = [('sale_ok', '=', True)]
            else:
                order.domain1 = [('sale_ok', '=', False)]
                
                
    @api.onchange('type_of_service')
    def onchange_receiving_type(self):
        b={'domain': {'product_id': [('sale_ok', '=', 0),('purchase_ok', '=', 0)]}}
        if self.type_of_service=='air':
            b ={'domain': {'product_id': [('sale_ok', '=', 1)]}}
        if self.type_of_service=='land':
            b ={'domain': {'product_id': [('sale_ok', '=', 0)]}}
        if self.type_of_service=='ocaen':
            b ={'domain': {'product_id': [('purchase_ok', '=', 1)]}}
   
        return b
            

    
    
