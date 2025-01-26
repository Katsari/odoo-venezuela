{
    "name": "Binaural Reportes/filtros de Ubicacion",
    "summary": """
        Reportes localizacion 
    """,
    "license": "LGPL-3",
    "author": "Binauraldev",
    "website": "https://binauraldev.com/",
    "category": "Accounting/Accounting",
    "version": "17.0.1.0.0",
    "depends": [
        "base",
        "contacts",
        "binaural_sale",
        "binaural_accountant",
        "binaural_seller",
        "binaural_location",
    ],
    "data": [
        "report/account_invoice_report .xml",
        "report/sale_order.xml",
        "report/sale_report.xml",
        "report/account_move.xml"
    ],
    "application": True,
    "binaural": True,
}
