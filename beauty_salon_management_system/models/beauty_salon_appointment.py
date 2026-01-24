from odoo import models, fields, api
from datetime import datetime, timedelta

class BeautySalonAppointment(models.Model):
    _name = 'beauty_salon.appointment'
    _description = 'Scheduled appointment for a client'
    _order = 'appointment_date desc'
    
    name = fields.Char(string='Appointment Reference', compute='_compute_name', store=True, readonly=True)
    client_id = fields.Many2one('beauty_salon.client', string='Client', required=True, ondelete='cascade')
    service_id = fields.Many2one('beauty_salon.service', string='Service', required=True)
    staff_id = fields.Many2one('beauty_salon.staff', string='Assigned Staff', required=True)
    appointment_date = fields.Datetime(string='Appointment Date & Time', required=True, default=lambda self: fields.Datetime.now())
    duration = fields.Integer(string='Duration (minutes)', required=True, default=60)
    end_date = fields.Datetime(string='End Date & Time', compute='_compute_end_date', store=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ], string='Status', default='draft', readonly=True, tracking=True)
    
    reason_for_cancel = fields.Text(string='Reason for Cancellation',
        help='Reason provided when appointment is cancelled.',
        readonly=True, states={'cancelled': [('readonly', False)]})
    
    @api.depends('appointment_date', 'duration')
    def _compute_end_date(self):
        for appointment in self:
            if appointment.appointment_date and appointment.duration:
                appointment.end_date = appointment.appointment_date + timedelta(minutes=appointment.duration)
            else:
                appointment.end_date = False
    
    @api.depends('client_id', 'appointment_date')
    def _compute_name(self):
        for appointment in self:
            if appointment.client_id and appointment.appointment_date:
                date_str = appointment.appointment_date.strftime('%Y%m%d')
                appointment.name = f"APPT-{date_str}-{appointment.client_id.name}"
            else:
                appointment.name = "New Appointment"
