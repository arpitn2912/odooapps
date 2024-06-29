# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class FacilityBooked(models.Model):
    _name = 'facility.booked'
    _description = 'Facility Booked'


    name = fields.Char(string='Name')
    availability_date_begin = fields.Date(string='Start Date')
    availability_date_end = fields.Date(string='End Date')
    number_of_person = fields.Integer(string='Number Of Person')
    facility_listings_id = fields.Many2one('facility.listings', string='Facility')
    state_id = fields.Many2one('res.country.state', string="State")
 
    state = fields.Selection(
        selection=[('draft', 'Draft'),
            ('approved', 'Approved'),
            ('cancelled', 'Cancelled')],
        string='Status',
        copy=False,
        default='draft')

    def cancelled(self):
        self.state = 'cancelled'
        
    def approved(self):
        if self.facility_listings_id:
            if self.facility_listings_id.is_limit_facility_providing:
                if self.facility_listings_id.number_of_people:
                     total_provide_facility = sum(self.facility_listings_id.facility_booked_ids.mapped('number_of_person'))
                     if self.facility_listings_id.number_of_people < total_provide_facility and self.facility_listings_id.state_id.id == self.state_id.id:
                         raise ValidationError(_('Not Avalible of Facility on %s Plase ! ',self.state_id.name))
        self.state = 'approved'
