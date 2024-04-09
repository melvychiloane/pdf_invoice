from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.units import inch


def invoice_details():

    invoice_number = input("Invoice number:\n")
    invoice_date = input("billing date:\n")
    Customer_id = input("Customer Id:\n")
    due_date = input("Due date:\n")
    return invoice_number, invoice_date, Customer_id,due_date

def add_pdf_elements():
    styles = getSampleStyleSheet()
    pdf_elements =[]
    invoice_info = invoice_details()
    pdf_elements.append(Paragraph("Invoice", styles['Title']))

    # Invoice details
    pdf_elements.append(Paragraph(f"Invoice Number: {invoice_info[0]}", styles['Heading3']))
    pdf_elements.append(Paragraph(f"Invoice Date: {invoice_info[1]}", styles['Normal']))
    pdf_elements.append(Paragraph(f"Customer ID: {invoice_info[2]}", styles['Normal']))
    pdf_elements.append(Paragraph(f"Due Date: {invoice_info[3]}", styles['Normal']))
    return pdf_elements

def items(products_list):
    data = [['Item', 'Quantity', 'Unit Price', 'Amount']]
    for item in products_list:
        data.append([item['Item'], str(item['Quantity']), str(item['Unit_price']), str(item['Amount'])])
    return data

def make_table(products_list):
    data = items(products_list)
    pdf_elements = add_pdf_elements()
    table_style = TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ('COLWIDTHS', (0, -1), (-1, -1), [100, 200, 150])])
    item_table = Table(data)
    item_table.setStyle(table_style)
    pdf_elements.append(item_table)
    return pdf_elements


def build_pdf(products_list, total_amount):
    pdf_elements = make_table(products_list)
    pdf_elements.append(Spacer(1, 12))
    styles = getSampleStyleSheet()
    pdf_elements.append(Paragraph(f"Total Amount: ${total_amount}", styles['Normal']))
    
    pdf_invoice = SimpleDocTemplate("invoice.pdf", pagesize=letter)
    pdf_invoice.build(pdf_elements)

