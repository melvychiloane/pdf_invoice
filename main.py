import items as items
import invoicegen as pdf


if __name__ == "__main__":
    products_list, total_amount = items.get_Total()
    pdf.build_pdf(products_list, total_amount)