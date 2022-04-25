from odoo import models, fields


class Courses(models.Model):
    _name = 'academy.courses'
    name = fields.Char()
    _inherit = 'mail.thread'

    teacher_id = fields.Many2one('academy.teachers', string='Teacher')