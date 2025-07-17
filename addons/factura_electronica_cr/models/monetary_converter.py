from odoo import api, fields, models, _
from odoo.tools.misc import get_lang
from markupsafe import Markup
import logging

_logger = logging.getLogger(__name__)


class MonetaryConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.monetary'

    @api.model
    def value_to_html(self, value, options):
        # Handle None or invalid value input
        if value is None:
            value = 0.0
        elif not isinstance(value, (int, float)):
            raise ValueError(_("The value send to monetary field is not a number."))

        # Get currency with multiple fallback levels
        display_currency = options.get('display_currency')
        if not display_currency:
            company_id = options.get('company_id', self.env.company.id)
            company = self.env[ 'res.company' ].browse(company_id)
            display_currency = company.currency_id

            if not display_currency:
                # Ultimate fallback - try USD first, then any available currency
                display_currency = self.env.ref('base.USD', raise_if_not_found=False) or \
                                   self.env[ 'res.currency' ].search([ ], limit=1)

                if not display_currency:
                    # This should never happen in a properly installed Odoo
                    _logger.error("No currency available for monetary field formatting")
                    return Markup('')

        # Get decimal places with proper fallbacks
        decimal_places = options.get('decimal_places')
        if decimal_places is None:
            decimal_places = getattr(display_currency, 'decimal_places', 2)

        fmt = "%.{0}f".format(decimal_places)

        # Handle currency conversion if from_currency is specified
        if options.get('from_currency'):
            date = options.get('date') or fields.Date.today()
            company_id = options.get('company_id', self.env.company.id)
            company = self.env[ 'res.company' ].browse(company_id)
            try:
                value = options[ 'from_currency' ]._convert(
                    value, display_currency, company, date)
            except Exception as e:
                _logger.warning("Currency conversion failed: %s", str(e))
                # Continue with original value if conversion fails

        # Format the amount
        lang = get_lang(self.env)
        formatted_amount = lang.format(
            fmt,
            display_currency.round(value),
            grouping=True
        ).replace(r' ', '\N{NO-BREAK SPACE}').replace(r'-', '-\N{ZERO WIDTH NO-BREAK SPACE}')

        # Prepare currency symbol positioning
        pre = post = ''
        currency_position = getattr(display_currency, 'position', 'after')

        if currency_position == 'before':
            pre = '{symbol}\N{NO-BREAK SPACE}'.format(symbol=display_currency.symbol or '')
        else:
            post = '\N{NO-BREAK SPACE}{symbol}'.format(symbol=display_currency.symbol or '')

        # Special formatting for label prices
        if options.get('label_price') and lang.decimal_point in formatted_amount:
            sep = lang.decimal_point
            integer_part, decimal_part = formatted_amount.split(sep, 1)
            integer_part += sep
            return Markup(
                '{pre}<span class="oe_currency_value">{0}</span>'
                '<span class="oe_currency_value" style="font-size:0.5em">{1}</span>'
                '{post}'
            ).format(integer_part, decimal_part, pre=pre, post=post)

        # Standard formatting
        return Markup('{pre}<span class="oe_currency_value">{0}</span>{post}').format(
            formatted_amount, pre=pre, post=post)