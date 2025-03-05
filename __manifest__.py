{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manage students, courses, schedules, and grades',
    'description': 'A module to manage school students, courses, schedules, and grades.',
    'author': 'Abraham',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/school_student_views.xml',  # Chargé en premier
        'views/school_course_views.xml',
        'views/school_schedule_views.xml',
        'views/school_grade_views.xml',
        'views/school_menu_views.xml',    # Chargé en dernier
        'data/school_data.xml',
    ],
    'demo': [
        'data/school_data.xml',
    ],
    'installable': True,
    'application': True,
}