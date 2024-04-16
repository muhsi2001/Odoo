from odoo import api, models


class HrAttendanceReport(models.AbstractModel):
    _name = 'report.day_wise_attendance.report_attendance'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('qwe', data)
        return {'doc_ids': docids,
                'data': data,
                }
