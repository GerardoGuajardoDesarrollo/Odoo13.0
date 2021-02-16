from odoo import api,fields,models

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.depends('origin','reference')
    def _compute_production_id(self):
        for rec in self:
            production_id = self.env['mrp.production'].search([(
                'product_id','=', rec.product_id.id),(
                    'name','=',rec.reference)])
            if not production_id:
                pass
            rec.production_id = production_id.id

    production_id = fields.Many2one(
        'mrp.production',
        check_company=True,
        compute ='_compute_production_id')