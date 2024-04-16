{
    'name': 'Day Wise Attendance',
    'depends':['hr_attendance'],
    'data':[
        'security/ir.model.access.csv',
        'report/day_wise_report.xml',
        'views/hr_attendance_views.xml',
        'views/attendance_views.xml',
        'wizards/attendance_report_views.xml',
        'report/ir_action_report_hr_attendance.xml',
    ]
}