from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BeautySalonClient(models.Model):
    _name = 'beauty.salon.client'
    _description = 'Client or customer of the beauty salon'
    
    name = fields.Char("Client Name", required=True)
    partner_id = fields.Many2one('res.partner', string='Contact', required=True,
                                 help="Link to the contact in Odoo's partner system")
    date_of_birth = fields.Date("Date of Birth")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
    notes = fields.Text("Client Notes")
    active = fields.Boolean("Active", default=True)
    create_date = fields.Datetime("Created On", readonly=True)
    
    # Salon relationship
    salon_id = fields.Many2one('beauty.salon', string='Salon', required=True, 
                               default=lambda self: self._default_salon_id())
    
    # Membership status
    membership_status = fields.Selection([
        ('none', 'No Membership'),
        ('basic', 'Basic Member'),
        ('premium', 'Premium Member'),
        ('vip', 'VIP Member')
    ], string="Membership Status", default='none')
    
    # Related fields from partner
    phone = fields.Char(related='partner_id.phone', string="Phone Number", readonly=True)
    email = fields.Char(related='partner_id.email', string="Email Address", readonly=True)
    address = fields.Text(related='partner_id.contact_address_complete', string="Full Address", readonly=True)
    
    # Computed fields for display
    @api.depends('partner_id')
    def _compute_contact_info(self):
        for client in self:
            client.phone = client.partner_id.phone
            client.email = client.partner_id.email
            client.address = client.partner_id.contact_address_complete
    
    # Default methods
    def _default_salon_id(self):
        # Return the first salon if exists, otherwise False
        salon = self.env['beauty.salon'].search([], limit=1)
        return salon.id if salon else False
    
    # Constraints
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for client in self:
            if client.date_of_birth and client.date_of_birth > fields.Date.today():
                raise ValidationError("Date of birth cannot be in the future!")
    
    # Override create to ensure partner exists
    @api.model
    def create(self, vals):
        # If partner_id is not provided, create a new partner
        if 'partner_id' not in vals:
            partner_vals = {
                'name': vals.get('name', 'New Client'),
                'company_type': 'person',
            }
            partner = self.env['res.partner'].create(partner_vals)
            vals['partner_id'] = partner.id
        return super(BeautySalonClient, self).create(vals)
    
    def write(self, vals):
        # Update partner name if client name changes
        if 'name' in vals and 'partner_id' not in vals:
            for client in self:
                client.partner_id.write({'name': vals['name']})
        return super(BeautySalonClient, self).write(vals)
