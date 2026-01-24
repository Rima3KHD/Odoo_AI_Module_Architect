from odoo import models, fields, api

class BeautySalonStaff(models.Model):
    _name = 'beauty_salon.staff'
    _description = 'Employee or service provider at the salon'
    
    name = fields.Char("Staff Name", required=True)
    phone = fields.Char("Phone Number")
    email = fields.Char("Email Address")
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
    
    @api.depends()
    def _compute_appointment_count(self):
        for staff in self:
            staff.appointment_count = self.env['beauty_salon.appointment'].search_count([('staff_id', '=', staff.id)])
    
    def action_open_appointments(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Staff Appointments',
            'res_model': 'beauty_salon.appointment',
            'view_mode': 'tree,form,calendar',
            'domain': [('staff_id', '=', self.id)],
            'context': {'default_staff_id': self.id},
        }