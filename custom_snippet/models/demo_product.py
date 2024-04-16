# -*- coding: utf-8 -*-

from odoo import fields, models

class DemoProduct(models.Model):
    _name= 'demo.product'

    name = fields.Char('name')