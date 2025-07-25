from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Préstamo de Libro'

    member_id = fields.Many2one('library.member', string='Socio', required=True)
    book_id = fields.Many2one('library.book', string='Libro', required=True)
    loan_date = fields.Date(string='Fecha de Préstamo', default=fields.Date.today, required=True)
    return_date = fields.Date(string='Fecha de Devolución')
    state = fields.Selection([
        ('borrowed', 'Prestado'),
        ('returned', 'Devuelto'),
    ], string='Estado', default='borrowed', required=True)

    # Regla de negocio: no más de 5 libros simultáneos
    @api.constrains('member_id', 'state')
    def _check_max_loans(self):
        for loan in self:
            if loan.state == 'borrowed':
                count = self.env['library.loan'].search_count([
                    ('member_id', '=', loan.member_id.id),
                    ('state', '=', 'borrowed'),
                    ('id', '!=', loan.id)
                ])
                if count >= 5:
                    raise ValidationError('El socio ya tiene 5 préstamos activos.')
    def action_return(self):
        for loan in self:
            loan.write({
                'state': 'returned',
                'return_date': fields.Date.today()
            })
           
