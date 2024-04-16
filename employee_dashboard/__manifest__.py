# -*- coding: utf-8 -*-
{
    'name': 'Employee Dashboard',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Employee Dashboard',
    'author': "Mike",
    'description': "Employee Dashboard",
    'depends': ['hr','hr_attendance','project','hr_holidays','hr_contract','hr_payroll_community'],
    'data': [
        'views/employee_client_action.xml',
        'views/employee_menu.xml',
        'views/hr_contract_views.xml',
        'views/hr_employee_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'employee_dashboard/static/src/js/dashboard.js',
            'employee_dashboard/static/src/css/dashboard.css',
            'employee_dashboard/static/src/xml/dashboard.xml',
        ],
    },
}