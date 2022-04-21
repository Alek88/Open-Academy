from odoo import models, fields


class Openacademy_Partner(models.Model):
    # наследование
    _inherit = 'res.partner'
    _description = 'res.partner'
    inh_instructor = fields.Boolean(string='Instructor')
    inh_sessions = fields.Many2many(
        string='Sessions',
        comodel_name='openacademy.sessions'
    )
    inh_teacher = fields.Many2one(
        'openacademy.teacher',
         string='Teacher Level'
    )
