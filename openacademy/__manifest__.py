# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': "Courses Open Academy",

    'description': """
        
    """,

    'author': "ALEK SANDER",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Openacademy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'views/openacademy_course.xml',
            'views/openacademy_sessions.xml',
            'views/openacademy_inherit_partner.xml',
            'views/openacademy_teacher.xml',
            'report/openacademy_report.xml',
            'views/openacademy_dashboard.xml'
             ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
