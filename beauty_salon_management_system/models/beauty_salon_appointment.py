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
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', required=True)
    
    notes = fields.Text(string='Appointment Notes')
    
    @api.depends('client_id', 'service_id', 'appointment_date')
    def _compute_name(self):
        for appointment in self:
            if appointment.client_id and appointment.service_id and appointment.appointment_date:
                date_str = appointment.appointment_date.strftime('%Y-%m-%d')
                appointment.name = f"{appointment.client_id.name} - {appointment.service_id.name} - {date_str}"
            else:
                appointment.name = "New Appointment"
    
    @api.depends('appointment_date', 'duration')
    def _compute_end_date(self):
        for appointment in self:
            if appointment.appointment_date and appointment.duration:
                appointment.end_date = appointment.appointment_date + timedelta(minutes=appointment.duration)
            else:
                appointment.end_date = False
    
    def action_confirm(self):
        self.write({'state': 'confirmed'})
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_complete(self):
        self.write({'state': 'completed'})
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})
    
    def action_reset_to_draft(self):
        self.write({'state': 'draft'})