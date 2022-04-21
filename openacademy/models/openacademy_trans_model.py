from odoo import models, fields, api

# механизм вызова своего рода помощников для заполнения, формы, которые не хранят значения и сеществ до момента закрытия
class Trans_model(models.TransientModel):
    _name = 'openacademy.trans.model'

    def _default_session(self):
        return self.env['openacademy.sessions'].browse(self._context.get('active_id'))

    trans_session = fields.Many2one('openacademy.sessions', string='Session', default=_default_session)
    trans_partner = fields.Many2many('res.partner', string='Partners')

    def add_partner_list(self):
        for session in self.trans_session:
            session.participants |= self.trans_partner
        return {}
