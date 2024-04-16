from odoo import api, models


class FleetAuctionReport(models.AbstractModel):
    _name = 'report.fleet_auction.report_auction'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('qwe',data)
        return {'doc_ids': docids,
                'data': data,
                }
