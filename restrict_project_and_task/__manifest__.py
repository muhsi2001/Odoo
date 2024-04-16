# -*- coding: utf-8 -*-
{
    'name': 'Restrict Project and Task',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Restrict Project and Task',
    'author': "Joe",
    'description': "Restrict Project and Task",
    'depends':['base','project'],
    'data':[
        'security/project_and_task_security.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
    ]
}