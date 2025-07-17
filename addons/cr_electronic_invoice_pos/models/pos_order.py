# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
from datetime import datetime
from markupsafe import Markup
from itertools import groupby
from collections import defaultdict
from random import randrange
from pprint import pformat

import psycopg2
import pytz

from odoo import api, fields, models, tools, _, Command
from odoo.tools import float_is_zero, float_round, float_repr, float_compare, formatLang
from odoo.exceptions import ValidationError, UserError
from odoo.osv.expression import AND
import base64


_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = 'pos.order'

    qr_image = fields.Binary(string='QR Code', readonly=True,compute='_compute_qr_image')
    number_electronic = fields.Char(string="Electronic Number", copy=False, index=True)
    account_move_name = fields.Char(string="Account Move Name", copy=False, index=True)


    @api.depends('account_move')
    def _compute_qr_image(self):
        for order in self:
            if order.account_move:
                order.qr_image = order.account_move.qr_image
                order.account_move_name = order.account_move.name
                order.number_electronic = order.account_move.number_electronic
            else:
                order.qr_image = False
                order.number_electronic = 'Empty'

    def _prepare_invoice_vals(self):
        res = super(PosOrder, self)._prepare_invoice_vals()
        payment_method_id = self.payment_ids.mapped('payment_method_id')
        res['payment_methods_id'] = payment_method_id.id if payment_method_id else False
        return res