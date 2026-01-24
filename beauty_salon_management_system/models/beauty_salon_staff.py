from odoo import models, fields, api

class BeautySalonStaff(models.Model):
    _name = 'beauty_salon.staff'
    _description = 'Employee or service provider at the salon'
    
    name = fields.Char("Staff Name", required=True)
    phone = fields.Char("Phone Number")
    email = fields.Char("Email Address")
    emergency_contact = fields.Char("Emergency Contact")
    specialization = fields.Selection([
        ('hair_stylist', 'Hair Stylist'),
        ('nail_tech', 'Nail Technician'),
        ('esthetician', 'Esthetician'),
        ('makeup_artist', 'Makeup Artist'),
        ('massage_therapist', 'Massage Therapist'),
        ('general', 'General Staff')
    ], string="Specialization", default='general')
    hire_date = fields.Date("Hire Date", default=fields.Date.today)
    job_title = fields.Char("Job Title")
    active = fields.Boolean("Active", default=True)
    notes = fields.Text("Staff Notes")
    
    # Computed fields
    appointment_count = fields.Integer("Appointments", compute='_compute_appointment_count', store=False)
    
    