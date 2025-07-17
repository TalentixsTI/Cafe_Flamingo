# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for move in self:
            if move.pos_order_ids:
                for pos in self.pos_order_ids:
                    pos.number_electronic = move.name
                    pos.qr_image = move.qr_image

        return res