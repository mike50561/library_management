from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Socio de biblioteca"
    _order = "member_code"

    name = fields.Char(string="Nombre", required=True)
    join_date = fields.Date(
        string="Fecha Alta",           # ← etiqueta mejorada
        default=fields.Date.context_today,
        readonly=True,
    )
    member_code = fields.Char(
        string="Código de socio",
        readonly=True,
        copy=False,
        index=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Genera un código único con prefijo SOC + 4 dígitos."""
        for vals in vals_list:
            vals['member_code'] = self.env['ir.sequence'].next_by_code('library.member') or _('SOC0000')
        return super().create(vals_list)

    _sql_constraints = [
        (
            'member_code_unique',
            'unique(member_code)',
            'El código de socio debe ser único.',
        ),
    ]
