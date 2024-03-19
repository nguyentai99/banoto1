from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle


def in_hoa_don():
    # Sample data for the invoice
    invoice_data = {
        'items': [
            {'product_id': 'P001', 'product_name': 'Product A', 'quantity': 2, 'unit_price': 50, 'total': 100},
            {'product_id': 'P002', 'product_name': 'Product B', 'quantity': 1, 'unit_price': 70, 'total': 70},
            {'product_id': 'P003', 'product_name': 'Product C', 'quantity': 3, 'unit_price': 30, 'total': 90}
        ],
        'total': 260,
        'tennv': 'Tran Tri Trung'
    }

    # Generate the invoice PDF from the data and save it to a file
    create_invoice_pdf(invoice_data, 'invoice.pdf')


def create_invoice_pdf(invoice_data, filename):
    # Create a new PDF template
    pdf = SimpleDocTemplate(filename, pagesize=letter)

    # Create text styles for the text in the PDF
    normal_style = ParagraphStyle(name='Normal', fontName='Helvetica')

    # Prepare data for the invoice table
    data = [['Product ID', 'Product Name', 'Quantity', 'Unit Price', 'Total']]
    for item in invoice_data['items']:
        data.append([item['product_id'], item['product_name'], item['quantity'], item['unit_price'], item['total']])

    # Create the invoice table from the data
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Prepare content to add to the PDF
    content = []
    content.append(table)
    content.append(Paragraph("Total: ${:.2f}".format(invoice_data['total']), normal_style))
    content.append(Paragraph(f"Employee Name: {invoice_data['tennv']}", normal_style))

    # Add the invoice to the PDF
    pdf.build(content)


if __name__ == "__main__":
    in_hoa_don()
