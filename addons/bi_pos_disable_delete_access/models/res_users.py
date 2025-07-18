
from datetime import datetime,timedelta,date
import dateutil.parser
from itertools import groupby
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.misc import formatLang
from odoo.tools import html2plaintext
import odoo.addons.decimal_precision as dp

class ResUsers(models.Model):
	_inherit = 'res.users'

	disable_delete_access = fields.Boolean()