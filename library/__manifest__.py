# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Library",
    "summary": "Module for managing a library",
    "version": "16.0.1.0.0",
    "category": "Sistema DOQ",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ['base', 'product', 'sale'],
    "data": [
        'views/library_book.xml',
        'views/library_res_partner.xml',
        'views/library_book_genre.xml',
        'views/library_audit.xml',
        'security/library_model_access.xml',
        'security/ir.model.access.csv',
        ],
   
}
