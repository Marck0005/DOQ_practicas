from odoo import models, fields, tools, api, _
from datetime import timedelta



class LibraryBookReport(models.Model):
    _name = 'library.book.report'
    _auto = False
    
    book_id = fields.Many2one('library.book', string='Book')
    sale_count = fields.Integer(string='Sale count')
    rent_count = fields.Integer(string='Rent count')
    
    
    def init(self):
        self.env.cr.execute('DROP TABLE IF EXISTS library_book_report')
        self.env.cr.execute('''
            CREATE TABLE library_book_report AS (
                SELECT
                    row_number() OVER () AS id,
                    b.id AS book_id,
                    COUNT(s.id) AS sale_count,
                    COUNT(r.id) AS rent_count
                FROM
                    library_book b
                    LEFT JOIN sale_order_line s ON (b.id = s.product_id)
                    LEFT JOIN library_book_rent r ON (b.id = r.book_id)
                GROUP BY
                    b.id
                

            )
        ''')
       

  
    
    