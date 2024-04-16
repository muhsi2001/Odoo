# -*- coding; utf-8 -*-
from odoo import models


class PosSession(models.Model):
   _inherit = 'pos.session'

   def _loader_params_res_partner(self):
       result = super()._loader_params_res_partner()
       result['search_params']['fields']+=['due_limit','due_amount']
       return result
