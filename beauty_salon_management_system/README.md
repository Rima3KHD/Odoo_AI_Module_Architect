# Beauty Salon Management System

A comprehensive Odoo 18 module for managing beauty salon operations including client management, service catalog, appointment scheduling, and staff management.

## Features

### 1. Client Management
- Complete client profiles with contact information
- Client notes and history tracking
- Unique email and phone validation
- Active/inactive client status

### 2. Service Catalog
- Service definitions with pricing and duration
- Service categories (Hair, Nails, Skin Care, Makeup, Spa, Other)
- Active/inactive service management
- Sequencing for display order

### 3. Staff Management
- Staff profiles with specialization
- Hire date and job title tracking
- Active/inactive status
- Appointment assignment

### 4. Appointment Scheduling
- Calendar integration for scheduling
- Multiple appointment states (Draft, Confirmed, In Progress, Completed, Cancelled)
- Automatic end time calculation
- Staff assignment and client linking

### 5. Security
- Granular access controls
- User vs Manager permissions
- Read/Write/Create/Delete permissions by role

## Installation

1. Copy the `beauty_salon_management_system` folder to your Odoo addons directory
2. Update the addons path in Odoo configuration if needed
3. Restart Odoo server
4. Go to Apps menu, search for "Beauty Salon Management System"
5. Click Install

## Configuration

After installation:
1. Go to Beauty Salon → Configuration → Services to set up your service catalog
2. Add staff members under Beauty Salon → Staff
3. Start adding clients under Beauty Salon → Clients
4. Schedule appointments using the calendar view

## Demo Data

The module includes demo data with:
- 3 sample clients
- 5 sample services
- 3 sample staff members
- 3 sample appointments

## Dependencies

- base
- web
- calendar

## Technical Information

- Version: 18.0.1.0.0
- Category: Services
- License: LGPL-3

## Support

For issues or questions, please contact your system administrator or refer to the Odoo documentation.
