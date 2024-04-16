# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime


class HrContract(models.Model):
    _inherit = "hr.contract"

    experience_years = fields.Integer(
        'Experience Years', compute='_compute_experience', store=True)

    @api.depends('date_start')
    def _compute_experience(self):
        """function defined to compute the experience of employees
        based on their joining date."""
        for contract in self:
            start_date = fields.Datetime.from_string(contract.date_start)
            start_year = int(start_date.strftime("%Y"))
            current_date = datetime.now()
            current_year = int(current_date.strftime("%Y"))
            experience_year = current_year - start_year
            print('***', experience_year)
            contract.experience_years = experience_year
