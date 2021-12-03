# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2019 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Website Quote Template Monthly',
    'author': 'Vertel AB',
    'category': 'Sales',
    'licence': 'AGPL-3',
    'version': '14.0.1.0.0',
    'website': 'https://www.vertel.se',
    'description': """
More features for online quotation
==================================

* Product image in pricing
* Product detail description for quotation
* New unit of measure month
* Additional table for monthly cost products
""",
    'depends': ['sale_quotation_builder'],
    'data': [
        'data/data.xml',
        'views/template.xml',
    ],
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4: