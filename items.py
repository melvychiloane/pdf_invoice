from reportlab.pdfgen import canvas
import collections

def input_format():
    data_file = input("Enter the file name containing data or press Enter to enter the item on the terminal: ")
    
    if data_file:
        try:
            with open(data_file, "r") as read_items:
                products = read_items.readlines()
                print("Products read from file:", products)
                return products
        except FileNotFoundError:
            print("File not found. Please make sure the file name and extension are correct and try again.")
            return 1
        except Exception as e:
            print("An error occurred:", e)
            return 2
    else:
        # If no file name is provided, read items from standard input (terminal)
        print("Enter items, one per line. Press Enter on an empty line to finish.")
        products = []
        while True:
            item = input("Item: ")
            if not item:
                break
            products.append(item)
        return products


def get_products():
    products = input_format()
    print("this is: " ,products)
    if products == "std_in":
        print("Inside the if statement")
        try:
            print("inside try")
            products_list = input("Enter items names : prices separated by commas ").split(", ")
            print("Done taking input")
            return products_list
        except:
            EOFError("No input recieved from starndard input")
    elif not None:
        return products
    else:
        return ("no product list")


def get_quantity():
    products = get_products()
    items_set = list(set(products))
    items_dict_list = []
    for i in range(len(items_set)):
        items_dict = {}
        item_name, unit_price = items_set[i].split(" ")
        quantity = products.count(items_set[i])
        items_dict["Item"] = item_name 
        items_dict["Unit_price"] = int(unit_price)
        items_dict["Quantity"] = quantity
        items_dict["Amount"] = int(unit_price)*int(quantity)

        items_dict_list.append(items_dict)
    return items_dict_list

def get_Total():
    items = get_quantity()
    sum = 0

    for each in items:
        sum += each["Amount"]
    return items, sum




if __name__ == "__main__":
    print(get_Total())