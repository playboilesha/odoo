# -*- coding: utf-8 -*-
from odoo import models,fields



class HrEmployeeWithIBAN(models.Model):
    _inherit = ['hr.employee']
    iban = fields.Char(string="IBAN",
                        store=True,
                        readonly=False)