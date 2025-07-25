from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Catálogo de Libros'

    title = fields.Char(string='Título', required=True)
    author = fields.Char(string='Autor', required=True)
    publication_date = fields.Date(string='Fecha de Publicación', required=True)
    age = fields.Integer(string='Antigüedad (años)', compute='_compute_age', store=True)
    loan_ids = fields.One2many('library.loan', 'book_id', string='Préstamos')
    isbn = fields.Char(string='ISBN', required=True) 
    disponible = fields.Boolean(string='Disponible', compute='_compute_disponible', store=True)

    @api.depends('publication_date')
    def _compute_age(self):
        for record in self:
            if record.publication_date:
                years = fields.Date.today().year - record.publication_date.year
                pub = record.publication_date
                today = fields.Date.today()
                if (today.month, today.day) < (pub.month, pub.day):
                    years -= 1
                record.age = years
            else:
                record.age = 0

    @api.depends('loan_ids.state')
    def _compute_disponible(self):
        for record in self:
            activo = any(loan.state == 'borrowed' for loan in record.loan_ids)
            record.disponible = not activo

    def action_create_loan(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Nuevo Préstamo',
            'res_model': 'library.loan',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_book_id': self.id,
            },
        }

