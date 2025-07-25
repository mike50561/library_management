from odoo import http
from odoo.http import request

class LibraryApiController(http.Controller):

    @http.route('/api/library/book/<string:isbn>', type='json', auth='public', methods=['GET'])
    def get_book_by_isbn(self, isbn):
        book = request.env['library.book'].sudo().search([('isbn', '=', isbn)], limit=1)
        if not book:
            return {'error': 'Libro no encontrado'}

        return {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'publication_date': str(book.publication_date),
            'isbn': book.isbn,
            'disponible': book.disponible
        }
