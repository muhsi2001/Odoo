from odoo import fields, models
from odoo.exceptions import UserError
import io
import json
import xlsxwriter
from odoo.tools import date_utils


class AuctionWizard(models.TransientModel):
    _name = 'auction.wizard'

    from_date = fields.Date(
        string='From Date',
        help='The wizard will generate report on and after this date')
    to_date = fields.Date(
        string='To Date',
        help='The wizard will generate report on and before this date')
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('confirmed', 'Confirmed'),
                   ('ongoing', 'Ongoing'),
                   ('success', 'Success'),
                   ('cancelled', 'Cancelled')],
        help='Stages of the auction')
    customer_id = fields.Many2one(string='Customer', comodel_name='res.partner',
                                  help='Customer participated in the auction')
    responsible_id = fields.Many2one(string='Responsible',
                                     comodel_name='res.users')

    def print_report(self):
        query = """select pr.name,p.name as user,fv.name as vehicle,fa.state,
         fa.start_price,fa.won_price,fa.start_date,
         fa.end_date from fleet_auction as fa
         left join res_partner as pr on pr.id = fa.customer_id
         inner join res_users as ur on ur.id = fa.responsible_id
         inner join res_partner as p on p.id = ur.partner_id
         left join fleet_vehicle as fv on fv.id = fa.vehicle_id where 1=1"""

        params = ()
        if self.from_date:
            query += """ AND start_date BETWEEN %s AND %s """
            params += (self.from_date, self.to_date)
        if self.customer_id:
            query += "  AND fa.customer_id = %s"
            params += (self.customer_id.id,)
        if self.state:
            query += " AND fa.state = %s"
            params += (self.state,)
        if self.responsible_id:
            query += " AND fa.responsible_id = %s"
            params += (self.responsible_id.id,)

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        data = {'report': report}
        print('aa', report)
        print('hgf', data)
        if report:
            return (self.env.ref('fleet_auction.action_report_fleet_auction').report_action(
                 None, data=data))
        else:
            raise UserError('No data to print')

    def print_xlsx_report(self):
        print('print_xlsx_report')
        query = """select pr.name,p.name as user,fv.name as vehicle,fa.state,
                 fa.start_price,fa.won_price,fa.start_date,
                 fa.end_date from fleet_auction as fa
                 left join res_partner as pr on pr.id = fa.customer_id
                 inner join res_users as ur on ur.id = fa.responsible_id
                 inner join res_partner as p on p.id = ur.partner_id
                 left join fleet_vehicle as fv on fv.id = fa.vehicle_id where 1=1"""

        params = ()
        if self.from_date:
            query += """ AND start_date BETWEEN %s AND %s """
            params += (self.from_date, self.to_date)
        if self.customer_id:
            query += "  AND fa.customer_id = %s"
            params += (self.customer_id.id,)
        if self.state:
            query += " AND fa.state = %s"
            params += (self.state,)
        if self.responsible_id:
            query += " AND fa.responsible_id = %s"
            params += (self.responsible_id.id,)

        self.env.cr.execute(query, params)
        report = self.env.cr.dictfetchall()
        # data = {'report': report}
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'fleet.auction',
                     'options': json.dumps(report,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Auction Excel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, report, response):
        print('get_xlsx_report')
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        sheet.set_column('D:R', 18)
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center', 'color': 'red'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px'})
        txt = workbook.add_format({'font_size': '10px', 'align': 'center'})
        sheet.merge_range('F2:I3', 'AUCTION REPORT', head)
        sheet.write('D5', 'Customer', cell_format)
        sheet.write('E5', 'Responsible', cell_format)
        sheet.write('F5', 'Fleet Name', cell_format)
        sheet.write('G5', 'State', cell_format)
        sheet.write('H5', 'Current Value', cell_format)
        sheet.write('I5', 'Won Amount', cell_format)
        sheet.write('J5', 'Start Date', cell_format)
        sheet.write('K5', 'End Date', cell_format)

        for i, rec in enumerate(report, start=7):
            sheet.write(f'D{i}', rec['name'], txt)
            sheet.write(f'E{i}', rec['user'], txt)
            sheet.write(f'F{i}', rec['vehicle'], txt)
            sheet.write(f'G{i}', rec['state'], txt)
            sheet.write(f'H{i}', rec['start_price'], txt)
            sheet.write(f'I{i}', rec['won_price'], txt)
            sheet.write(f'J{i}', rec['start_date'], txt)
            sheet.write(f'K{i}', rec['end_date'], txt)
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
