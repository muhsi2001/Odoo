# -*- coding: utf-8 -*-

from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = "project.project"

    # access_limited_users_id = fields.Many2one(
    #     string='Access Limited Users', comodel_name='res.users')

    limited_users_id = fields.Many2one(
        string='Access Limited Users', comodel_name='res.users')
