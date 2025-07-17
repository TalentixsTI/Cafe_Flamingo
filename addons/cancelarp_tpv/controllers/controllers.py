# -*- coding: utf-8 -*-
# from odoo import http


# class CancelarpTpv(http.Controller):
#     @http.route('/cancelarp_tpv/cancelarp_tpv', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cancelarp_tpv/cancelarp_tpv/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cancelarp_tpv.listing', {
#             'root': '/cancelarp_tpv/cancelarp_tpv',
#             'objects': http.request.env['cancelarp_tpv.cancelarp_tpv'].search([]),
#         })

#     @http.route('/cancelarp_tpv/cancelarp_tpv/objects/<model("cancelarp_tpv.cancelarp_tpv"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cancelarp_tpv.object', {
#             'object': obj
#         })

