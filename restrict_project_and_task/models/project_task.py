# -*- coding: utf-8 -*-

from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = "project.task"

    limited_users_id = fields.Many2one(
        string='Access Limited Users', comodel_name='res.users')
