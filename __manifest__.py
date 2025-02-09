{
    'name': 'school System',
    'version': '1.2',
    'summary': 'cheeter System',
    'sequence': -100,
    'author': 'Nadeemkhan',
    'description': """ cheeter System""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/app/invoicing',

    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'web','report_xlsx'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/course_data.xml',
        'data/student_data.xml',
        'views/school.xml',
        'views/teacher.xml',
        'views/student.xml',
        'views/course.xml',
        'reports/report.xml',
        'reports/student_report_template.xml',
        'reports/teacher_report_template.xml',
        'reports/course_report_template.xml',

    ],
    'installable': True,
    'application': True,
    'auto_Install': False,
}
