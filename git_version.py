# ========================================= OOP INVENTORY SYSTEM ========================================= #

from tabulate import tabulate

# ================================================ CLASS ================================================= #

# Initialize shoes class with parameters country, code, product, cost, quantity
# Define functions for each parameter for the purpose of searching
# Define __str__ that returns object as a string

class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def set_quantity(self, new_quant):
        self.quantity = new_quant

    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()

# ====================================================== FUNCTIONS =============================================== #

# Open files in different formats
# Set empty lists for shoes list and object list 

inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")

items_list = []
shoe_obj = []

# Use try/finally in case the file does not open on user end
# Define read_shoes_data() that reads each line from the text file
# Append items onto empty list
# Cast each item into an object and append to object list

def read_shoes_data():
    file = None
    try:
        for lines in inventory_read:
            strip_lines = lines.strip("\n")
            split_lines = strip_lines.split(",")
            items_list.append(split_lines)

        for i in range(1, len(items_list)):
            array = items_list[i]
            shoe1 =  Shoes(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(shoe1)

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

# Use try/finally in case the file does not open on user end
# Define capture_shoes() that gets input from user for new products
# Cast each item into an object and append to object list
# Write to file, close file

def capture_shoes():
    
    file = None

    try:
        new_country = input("Please enter the country of your product:\n")
        new_code = input("Please enter the code of your product:\n")
        new_product = input("Please enter the name of your product:\n")
        new_cost = int(input("Please enter the cost of your product, only in numbers. E.g. 12345\n"))
        new_quantity = int(input("Please enter the quantity of your product, only in numbers. E.g. 2\n"))

        new_shoe = Shoes(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(new_shoe)

        inventory_write.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print("\nThank you, your product has been loaded!\n")

        inventory_write.close()

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

# Use try/finally in case the file does not open on user end
# Define view_all() that displays all shoes in console
# Get info for each product using get_() class methods
# Display using tabulate

def view_all():

    file = None
    
    try:

        print("\n---------------------------------------------STOCKLIST---------------------------------------------\n")

        country = []
        code = []
        product = []
        cost = []
        table  = []
        quantity = []

        for lines in shoe_obj:
            country.append(lines.get_country())
            code.append(lines.get_code())
            product.append(lines.get_product())
            cost.append(lines.get_cost())
            quantity.append(lines.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid'))

        print("\n---------------------------------------------END-------------------------------------------------\n")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

# Use try/finally in case the file does not open on user end
# Define restock() that displays first 5 items with lowest stock, using sort()
# Get info for each product using get_() class methods
# Display using tabulate
# Get input for new stock quantity
# Write to file and close

def restock():

    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table  = []

    try:
        shoe_obj.sort(key=lambda x:x.quantity)

        for i in range(1,6):
            restock_list.append(shoe_obj[i])
    
        print("\n----------------------------Lowest stock items:----------------------------\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='fancy_grid', showindex= range(1,6)))
        
        print("\n---------------------------------------------------------------------------\n")

        user_input_item = int(input("\nPlease confirm the index of the product you want to restock:\n"))
        user_input_qty = int(input("\nPlease confirm the new quantity:\n"))
        shoe_obj[user_input_item].set_quantity(user_input_qty)

        output = ''
        for item in shoe_obj:
            output += (f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print("\nYour product has been updated!")

    except FileNotFoundError as error:
        print("\nSorry, this file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()

# Define search_shoe() that displays specific shoe
# Get info for product using get_() class methods
# Display in console

def search_shoe():

    search_shoe = input("\nPlease enter the code you are searching for:\n\n")

    for line in shoe_obj:
        if line.get_code() == search_shoe:
            print(f'\n {line}')

    print("\nPlease select another option from the menu below\n")

# Define value_per_item() that displays value for specific shoe
# Get info for product using get_() class methods
# Display in console

def value_per_item():

    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} VALUE: R{value}\n')

# Define highest_quantity() that displays highest quantity
# Set empty list for quantity values
# Append values to list
# Display in console, using max()
# Mark item on sale

def highest_quantity():

    highest_qty = []

    for line in shoe_obj:
        highest_qty.append(line)

    print("\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoe_obj, key=lambda item: item.quantity))
    print("\nThis item has now been marked on sale\n")
    print("\nPlease select an option from the menu below")

# ====================================================== OUTPUT =============================================== #

# Display menu options
# Use try/finally in case the file does not open on user end
# Set ValueError
read_shoes_data()
while True:

    try:
        menu = int(input('''\n
            Welcome to HyperionDev Inventory System! 
            Please select from the menu below:
            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_quantity()

        elif menu > 6:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")
        
# ====================================================== END =============================================== #