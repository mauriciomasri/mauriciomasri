{
    'name': 'Recorridos',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Recorridos de obra: el técnico marca las salidas en el plano y el PDF se guarda en Odoo',
    'author': 'Automa',
    'depends': ['base', 'mail', 'sale', 'base_automation'],
    'data': [
        'data/models.xml',
        'data/automation.xml',
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
