# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    experience = fields.Integer(
        'Experience', related='contract_ids.experience_years')

    @api.model
    def get_tiles_data(self):
        """ Function defined to return the tile and table data"""
        attendance = self.env['hr.attendance'].search_count([])
        project = self.env['project.project'].search_count([])
        task = self.env['project.task'].search_count([])
        leave = self.env['hr.leave'].search_count([])
        payslip = self.env['hr.payslip'].search_count([])
        hierarchy = self.search_count([])

        employee = self.search([], limit=10)
        name = employee.mapped('name')
        email = employee.mapped('private_email')
        phone = employee.mapped('private_phone')
        gender = employee.mapped('gender')
        cert = employee.mapped('certificate')
        study = employee.mapped('study_field')
        experience = employee.mapped('experience')

        return {
            'total_attendance': attendance,
            'total_project': project,
            'total_task': task,
            'total_leave': leave,
            'total_payslip': payslip,
            'total_hierarchy': hierarchy,
            'name': name,
            'email': email,
            'phone': phone,
            'gender': gender,
            'cert': cert,
            'study': study,
            'exp': experience
        }
