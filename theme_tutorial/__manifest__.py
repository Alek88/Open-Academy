{
    'name': 'Tutorial theme',
    'description': 'Learning theme create',
    'version': '1.0',
    'author': 'ALEK SANDER',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        "views/snippets.xml",
        "views/options.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_tutorial/static/scss/style.scss',
        ],
        'web.assets_primary_variables': [
            'theme_tutorial/static/scss/primary_variables.scss',
        ],
        'web.assets_frontend_helpers': [
            'theme_tutorial/static/scss/bootstrap_overridden.scss',
        ],
        'website.assets_editor': [
            'theme_tutorial/static/js/tutorial_editor.js',
        ]
    }

}