import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Sessions(models.Model):
    _name = 'openacademy.sessions'
    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start learning')
    end_date = fields.Date(string='End learning', compute="_end_date")
    duration = fields.Integer(string='Duration')
    number_of_seats = fields.Integer(string='Number of seats')
    occupied_of_seats = fields.Integer(string='Occupied', compute="_occupied_of_seats", store=True)
    active = fields.Boolean(string='Active', default=True)
    participants = fields.Many2many(string='Participants', comodel_name='res.partner')
    percentage_of_filling = fields.Integer(string='Parcentage of fillinf', compute='_percentage_of_filling')
    course = fields.Many2one('openacademy.course', string='Course')

    # domain (фильтруем список выбора по указанному условию)
    instructor = fields.Many2one(
        'res.partner',
        string='Instructor',
        domain=['|',
                    ('inh_instructor', '=', True),
                    '|',
                        ('inh_teacher.teacher_level', '=', 1),
                        ('inh_teacher.teacher_level', '=', 2)]
    )

    # depends (механизм определения значения переменной, заключенной в круглые скобки)
    @api.depends('participants')
    def _occupied_of_seats(self):
        for record in self:
            record.occupied_of_seats = len(record.participants)

    @api.depends('occupied_of_seats', 'number_of_seats')
    def _percentage_of_filling(self):
        for record in self:
            quantity = record.occupied_of_seats
            if quantity == 0 or (quantity== 0 and record.number_of_seats == 0):
                record.percentage_of_filling = 0
            else:
                record.percentage_of_filling = quantity / record.number_of_seats * 100

    @api.depends('start_date', 'duration')
    def _end_date(self):
        for record in self:
            if record.duration == 0:
                record.end_date = record.start_date
            else:
                record.end_date = record.start_date + datetime.timedelta(days=record.duration)

    # onchange (механизм проверки заполнения, если словами 1с - обработка события "При изменении")
    @api.onchange('number_of_seats', 'occupied_of_seats')
    def _control_number_of_seats(self):
        massage = ''
        is_error = False
        if self.number_of_seats < 0:
            massage = 'Отрицательные значения запрещены'
            is_error = True
        elif self.occupied_of_seats > self.number_of_seats:
            massage = 'Превышено количество участников группы'
            is_error = True

        if is_error:
            return {
                    'warning':{
                        'title': "Что-то пошло не так",
                        'message': massage
                }
            }

    #constrains (механизм проверки корректности заполнения формы элемента, языком 1с - при записи)
    @api.constrains('instructor', 'participants')
    def _instructor_in_participants(self):
        for record in self:
            if record.instructor in record.participants:
                raise ValidationError("Инструктор не может входить в список участников.")




