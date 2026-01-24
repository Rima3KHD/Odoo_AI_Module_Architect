from odoo import models, fields

class BeautySalonAppointment(models.Model):
    _name = 'beauty_salon.appointment'
    _description = 'Scheduled appointments for beauty salon services'

    
    client_id = fields.Many2one("Client", required=True)
    
    service_id = fields.Many2one("Service", required=True)
    
    staff_id = fields.Many2one("Assigned Staff", required=True)
    
    appointment_date = fields.Datetime("Appointment Date and Time", required=True)
    
    duration = fields.Integer("Duration (minutes)", required=True)
    
    notes = fields.Text("Appointment Notes")
    
    state = fields.Selection("Status", required=True)
    