# -*- coding: utf-8 -*-

from odoo import api, fields, models,_

class FacilityListings(models.Model):
    _name = 'facility.listings'
    _description = 'Facility Listings'

    name = fields.Char(string='Name')
    availability_date_begin = fields.Date(string='Start Date')
    availability_date_end = fields.Date(string='End Date')
    is_limit_facility_providing = fields.Boolean(string='Limit Facility Providing')
    number_of_people = fields.Integer(string='Number Of People')
    facility_booked_ids = fields.One2many('facility.booked', 'facility_listings_id')
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
        self.state = 'approved'
        
    def get_games(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Games',
            'view_mode': 'tree,form',
            'res_model': 'facility.booked',
            'domain': [('facility_listings_id', '=', self.id)],
            'context': "{'create': False}"
        }
