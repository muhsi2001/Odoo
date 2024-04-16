{
    'name': 'Custom Report',
    'version': '17.0.1.0.0',
    'category': 'Human Resources/Custom Report',
    'author': "Mike",
    'description': "Custom Report",
    'summary': "Manages fleet auction activities.",
    'depends': ['sale_management','stock'],
    'data': [
        'data/paper_format.xml',
        'report/report_layout.xml',
        'report/demo_report_templates.xml'
    ],
    'external_dependencies': {
        'python': ['matplotlib']
    }
}