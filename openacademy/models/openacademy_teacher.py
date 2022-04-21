from odoo import models, fields


class Teacher(models.Model):
    _name = 'openacademy.teacher'
    name = fields.Char(string='Name')
    teacher_level = fields.Integer(string='Teacher level')

