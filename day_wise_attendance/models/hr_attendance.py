# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrAttendance(models.Model):

    _inherit = "hr.attendance"

    check_in_date = fields.Date(
        string='Check In Date', compute='_compute_date', store=True)

    @api.depends('check_in')
    def _compute_date(self):
        for rec in self:
            rec.check_in_date = fields.Date.to_string(rec.check_in.date())
