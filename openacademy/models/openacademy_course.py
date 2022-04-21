from odoo import models, fields


class Openacademy_Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string='Course name')
    date_learning = fields.Date(string='Start learning', default=fields.Date.today())
    description = fields.Char(string='Description')
    sessions = fields.One2many('openacademy.sessions', string='sessions', inverse_name='course')
    responsible_user = fields.Many2one('res.users', string='Responsible user')

    # запрет создания элемента с таким же наименованием средствами SQL
    _sql_constraints = [
        ('name_mustbe_uniq',
         'UNIQUE(name)',
         'This name is already in use')
    ]

    # функция предназначена для изменения имени при копировании
    def copy(self, default=None):
        copy_name = 'Copy ' + self.name
        return super(Openacademy_Course, self).copy(dict(default or {}, name=copy_name))