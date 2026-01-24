from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'
    
    appointment_id = fields.Many2one(
        'beauty.salon.appointment',
        string='Appointment',
        help="Related beauty salon appointment",
        ondelete='set null',
        copy=False,
    )
