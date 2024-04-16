from odoo import models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def enable_automatic_invoice(self):
        self.write({
            'automatic_invoice': True
        })
