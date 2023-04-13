from datetime import date
from odoo import http

class TestModule2 (http.Controller):
    @http.route ('/test module4/belarusbank/', auth='user') 
    def index (self,**kw):
        data = ""
        employee_ids = http.request.env['hr.employee'].sudo().search([])
        for e in employee_ids:
            sum_wage = 0
            contract_ids = http.request.env['hr.contract'].sudo().search([])
            for c in contract_ids:
                if (c.state == "open" or c.state == 'draft') and c.employee_id == e and c.date_starts <= date.today():
                    try:
                        if c.date_end >= date.today():
                            sum_wage += c.wage
                    except:
                        sum_wage += c.wage
            if sum_wage > 0:
                data += str(e.iban) + " " + str(sum_wage) + " " + str(e.name) + "\n"
        res = http.Response()
        res.headers ['Content-Disposition'] = 'attachment; filename=belarusbank.txt'
        res.set_data(data) 
        return res