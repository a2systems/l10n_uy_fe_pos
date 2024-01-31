from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero, float_round, float_repr, float_compare
from odoo.exceptions import ValidationError, UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        vat_value = None
        if 'RUT' in vals.get('vat'):
            vals['l10n_latam_identification_type_id'] = self.env.ref('l10n_uy_fe.it_uy_rut').id
            vat_value = vals.get('vat').replace('RUT','')
            del vals['vat']
        if 'CI' in vals.get('vat'):
            vals['l10n_latam_identification_type_id'] = self.env.ref('l10n_uy_fe.it_uy_ci').id
            vat_value = vals.get('vat').replace('CI','')
            del vals['vat']
        #return super(ResPartner, self).with_context(no_vat_validation=True).create(vals)
        res = super(ResPartner, self).create(vals)
        if vat_value:
            vals = {'vat': vat_value} 
            return_id = res.write(vals)
        return res



    @api.constrains('vat', 'country_id')
    def check_vat(self):
        return True
