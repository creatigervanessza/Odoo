# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ResCompany(models.Model):
    _inherit = "res.company"
    
    
    picking_field_ids = fields.Many2many('ir.model.fields','picking_fields_company_rel', 'picking_id', 'company_id', string='Picking Fields', help="Fields configuration for Stock Picking QR Code generation")
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
