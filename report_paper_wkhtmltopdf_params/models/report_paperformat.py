# -*- coding: utf-8 -*-
# Copyright 2017 Avoin.Systems
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Paper(models.Model):
    _inherit = 'report.paperformat'

    custom_params = fields.One2many(
        'report.paperformat.parameter',
        'paperformat_id',
        'Custom Parameters',
        help='Custom Parameters passed forward as wkhtmltopdf '
             'command arguments'
    )