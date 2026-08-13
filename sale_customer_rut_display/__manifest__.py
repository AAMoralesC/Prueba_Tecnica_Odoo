{
    'name': 'Visualización del RUT del cliente en Ventas',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Muestra el RUT del cliente en los pedidos de venta',
    'description': """
        Este módulo agrega un campo de solo lectura que muestra el RUT del cliente en:
        - Vista formulario de Pedidos de Venta.
        - Vista lista de Pedidos de Venta (con capacidad de ordenar y filtrar).
    """,
    'author': 'Andres',
    'website': '',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
