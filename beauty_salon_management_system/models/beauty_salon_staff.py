from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BeautySalonStaff(models.Model):
    _name = 'beauty.salon.staff'
    _description = 'Employee or service provider at the salon'
    
    name = fields.Char("Staff Name", required=True)
    phone = fields.Char("Phone Number")
    email = fields.Char("Email Address")
    emergency_contact = fields.Char("Emergency Contact")
    
    # Salon relationship
    salon_ids = fields.Many2many('beauty.salon', string='Assigned Salons', 
                                 help='Salons where this staff member works')
    
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
    
    # Manager flag
    is_manager = fields.Boolean("Is Manager", default=False,
                                help="Check if this staff member can manage a salon")
    
    active = fields.Boolean("Active", default=True)
    notes = fields.Text("Staff Notes")
    
    # Computed fields
    appointment_count = fields.Integer("Appointments", compute='_compute_appointment_count', store=False)
    
    @api.depends()
    def _compute_appointment_count(self):
        for staff in self:
            staff.appointment_count = self.env['beauty.salon.appointment'].search_count([
                ('staff_id', '=', staff.id)
            ])
    
    @api.constrains('is_manager')
    def _check_manager_salons(self):
        for staff in self:
            if staff.is_manager:
                # Check if this manager is assigned to multiple salons
                manager_salons = self.env['beauty.salon'].search([
                    ('manager_id', '=', staff.id)
                ])
                if len(manager_salons) > 1:
                    raise ValidationError("A manager can only be assigned to one salon as manager!")
    
    def name_get(self):
        result = []
        for staff in self:
            name = staff.name
            if staff.job_title:
                name = f"{name} ({staff.job_title})"
            result.append((staff.id, name))
        return result