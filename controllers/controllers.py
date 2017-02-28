# -*- coding: utf-8 -*-
from odoo import http

# class Yebug(http.Controller):
#     @http.route('/yebug/yebug/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yebug/yebug/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('yebug.listing', {
#             'root': '/yebug/yebug',
#             'objects': http.request.env['yebug.yebug'].search([]),
#         })

#     @http.route('/yebug/yebug/objects/<model("yebug.yebug"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yebug.object', {
#             'object': obj
#         })