# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import UserError


class AttendanceReport(models.TransientModel):
    _name = 'attendance.report'

    attendance_date = fields.Date(
        string='Date',
        help='The wizard will generate report on and after this date')

    def print_report(self):

        query = """select em.name,dep.name as department,em.work_email,
                hr.check_in,hr.check_out,hr.worked_hours from
                hr_attendance as hr
                join hr_employee as em on em.id = hr.employee_id
                join hr_department as dep on dep.id = em.department_id
                where 1=1"""

        params = ()
        if self.attendance_date:
            query += "  AND hr.check_in_date = %s"
            params += (self.attendance_date,)

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        data = {'report': report,
                'attendance': self.attendance_date}
        if report:
            return (self.env.ref(
                'day_wise_attendance.action_report_hr_attendance').report_action(
                None, data=data))
        else:
            raise UserError('No data to print')
