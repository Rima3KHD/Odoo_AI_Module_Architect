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
        string='Appointment Date2',
        related='appointment_id.appointment_date',
        store=True,
        readonly=False,
        help="Date and time of the related appointment",
    )
    appointment_note = fields.Text(
        string='Appointment Note',
        help="Additional notes about the appointment",
        copy=False,
    )
    price_agreed = fields.Monetary(
        string='Price Agreed',
        currency_field='currency_id',
        help="Price agreed upon in the appointment",
        copy=False,
    )
