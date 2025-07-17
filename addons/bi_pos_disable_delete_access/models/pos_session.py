
from datetime import datetime,timedelta,date
import dateutil.parser
from itertools import groupby
from odoo import api, fields, models, _

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_res_users(self):
        result = super()._loader_params_res_users()
        result['search_params']['fields'].append('disable_delete_access')
        return result
