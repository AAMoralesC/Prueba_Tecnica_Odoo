{
    'name': 'Control Término de Pago en Clientes',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'Controla la asignación y edición del Término de Pago en clientes',
    'description': """
        Este módulo implementa reglas para el campo Término de pago en clientes:
        - Asigna "Pago inmediato" por defecto a nuevos clientes.
        - Restringe la edición a usuarios con rol de Administrador de Contabilidad.
        - Registra el historial de cambios en el Chatter.
    """,
    'author': 'Candidato Odoo',
    'depends': ['account'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
