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
    appointment_date = fields.Datetime(
        string='Appointment Date',
        related='appointment_id.appointment_date',
        store=True,
        readonly=False,
        help="Date and time of the related appointment",
    )
