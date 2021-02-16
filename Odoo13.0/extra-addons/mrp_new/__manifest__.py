# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Mrp_Stock_Move_Line',
    'version': '2.0',
    'website': 'www.pintacuario.mx',
    'category': 'Manufacturing/Manufacturing',
    'sequence': 16,
    'summary': 'Manufacturing Orders & BOMs',
    'depends': ['product', 'stock', 'resource'],
    'description': "",
    'data': [        
        'views/stock_move_line_mrp_view.xml',
    ],
    'qweb': ['static/src/xml/mrp.xml'],
    'demo': [
        'data/mrp_demo.xml',
    ],
    'test': [],
    'application': True,
}
