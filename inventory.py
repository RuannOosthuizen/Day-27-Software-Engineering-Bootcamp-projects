# Importing libraries.
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    # Here the initializer executes and create the instance level variables.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Here the method to return the cost of a shoe is defined.
    def get_cost(self):
        return self.cost

    # Here the method to produce the quantity of a product is defined.
    def get_quantity(self):
        return self.quantity

    # Here the method to return a string representation of the class is defined.
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============

# Here the function to open and read the "Inventory" text file is defined.
def read_shoes_data():

    # Here the error of the file not existing is handled with a try, except statement.
    try:
        with open("inventory.txt", "r") as file:

            # Here the first line of the text file is skipped.
            next(file)

            # Here each line of the file is read and stored in the "shoe_list".
            for lines in file:
                line = lines.strip()
                line = line.split(",")
                
                # Then the data from the text file is stored in the empty list.
                shoe_list.append(Shoe(line[0], line[1], line[2], line[3], int(line[4])))
            file.close()

    # If the file doesnt exist or is missing the user is informed.
    except:
        print("Sorry no file exists to read data from. Please create one.")


# Here the function to capture a new shoe is defined.
def capture_shoes():
    print("\n----------------------------Adding A New Shoe Product:----------------------------\n")

    # The text file is openned to write to it.
    inventory_write = open("inventory.txt", "a")

    # The user is able to enter the details of the new shoe to be added.
    country = input("Please enter the country the shoe is from:\t")
    code = input("Please enter the code of the shoe:\t")
    product = input("Please enter the product name:\t")
    cost = input("Please enter the price:\t")

    # Here the value of the quantity is checked to be valid inputs.
    while True:
        quantity = input("Please enter the stock amount:\t")
        if quantity.isnumeric():
            quantity = int(quantity)
            break
        else:
            print("\n Incorrect input, try again!\n")

    # Here the shoe object is created and added to the list.
    shoe_list.append(Shoe(country, code, product, cost, quantity))

    # Here the new shoe details are wtitten to the text file.
    inventory_write.write(f"{country},{code},{product},{cost},{quantity}\n")
    print("\nSuccess! The new shoe has been added to the inventory.")


# Here the function to view all the shoes
def view_all():
    print("\n----------------------------View All Product Details:----------------------------\n")

    # Here the read data from the text file is called.
    read_shoes_data()

    # Hhere the header and empty list is defined.
    header = ["Country", "Product Code", "Product Name", "Product Cost", "Quantity"]
    list_item = []

    # This for loop then iterates and stores a string version of the list in a new list of objects.
    for item in shoe_list:
        list_item.append(item.__str__())

    # Here the list of object is then converted into a list of lists for the tabulate module to work on.
    list_tabulate = [i.split(",") for i in list_item]

    # Then the tabulate version of the list is printed to the users.
    print(tabulate(list_tabulate, headers = header, tablefmt = "fancy_grid"))


# Here the function to find the lowst volume of stocked items is defined.
def re_stock():

    # Here the read data from the text file is called.
    read_shoes_data

    # Here the lowest value is found.
    min_quantity = min(pos.quantity for pos in shoe_list)

    # Then the product name is found and displayd to the user.
    for pos in shoe_list:
        if pos.quantity == min_quantity:
            print("\n----------------------------Item low in stock:----------------------------\n")
            print(f"Product:\t{pos.product}\nStock Count:\t{pos.quantity}\n")

            # Then the user is asked if they wish to restock the product or not.
            while True:
                choice = input("Do you wish to restock this itme? Y - Yes/No - N  ")
                if choice.lower() == "y":
                    while True:

                        # The user can then ad the new quantity to add to the current stock.
                        new_quantity = input("Enter quantity to add: ")
                        if new_quantity.isnumeric():
                            new_quantity = int(new_quantity)
                            break
                        else:
                            print('Wrong input, try again!')

                    # Then the new quantity is added to the current stock amount.
                    pos.quantity += new_quantity

                    # Then the updated details on the stock amount is written to the text file.
                    with open('inventory.txt', 'r') as list:
                        lines = list.readlines()
                    with open('inventory.txt', 'w') as list:
                        lines[shoe_list.index(pos)+1] = f"{pos.country},{pos.code},{pos.product},{pos.cost},{pos.quantity}\n"
                        list.writelines(lines)
                        list.close()
                    print("New stock value added.")
                    break

                elif choice.lower() == "n":
                    return
                else:
                    print("invalid input please try again.")
                    continue


# Here the function to view a certain shoe is defined.
def seach_shoe():
    print("\n----------------------------View Selected Product:----------------------------\n")

    # Here the read data from the text file is called.
    read_shoes_data()

    # The user can then input the product code.
    product_code = input("Please enter the code of the product:  ")

    # Then the for loop iterates through the list and compares the codes.
    for pos in shoe_list:
        if pos.code == product_code:
            print(f"\nProduct Details:\n {pos}")
            return

    print("Product not found, assure input is correct.")


# Here the function to view the value of each item in stock.
def value_per_item():
    print("\n----------------------------Value of Stock per Item:----------------------------\n")

    # Here the read data from the text file is called.
    read_shoes_data()

    # Here the for loop iterates through the list and extracts the cost and quantity
    # then calculates the total value.
    for pos in shoe_list:
        item_cost = pos.cost
        item_stock = pos.quantity
        total = int(item_cost) * item_stock
        print(f"{shoe_list.index(pos) + 1} {pos.product} - Total value: {total}")


# Here the function to view a product with the heighest quantity.
def highest_qty():

    # Here the read data from the text file is called.
    read_shoes_data()

    # Here the maximum quanityt is found.
    max_quantity = max(pos.quantity for pos in shoe_list)

    # Then then product name is found and displayed to the user.
    for pos in shoe_list:
        if pos.quantity == max_quantity:
            print("\n----------------------------Item heighest in stock:----------------------------\n")
            print(f"Product:\t{pos.product}\nStock Count:\t{pos.quantity}\n")
            print("\nThis item has now been marked on sale\n")
            return


#==========Main Menu=============

# Here the function to read the text file is called to create the list if the text file exists.
read_shoes_data()

print("\nWelcome to HyperionDev Inventory System!")

# Here the menu section is defined for the user selection.
while True:
    print('''Please select from the menu below:\n
    1 - Capture a new shoe
    2 - View all
    3 - Restock
    4 - Search a product
    5 - View Items Value
    6 - View Sale Item
    e - Exit''')
    menu = input("\t: ")

    # If the user selected "e", they exit the program.
    if menu.lower() == "e":
        print("Goodbye")
        break

    # If the user selected "1" they can then capture a new shoe to add to the list.
    elif int(menu) == 1:
        capture_shoes()

    # If the user selected "2" they can then view the entire inventory in  table format.
    elif int(menu) == 2:
        view_all()

    # If the user selected "3" they can then view the lowest stocked item and restock it.
    elif int(menu) == 3:
        re_stock()

    # If the user selected "4" they can then view a specified product.
    elif int(menu) == 4:
        seach_shoe()

    # If the user selected "5" they can then view the value of all items in stock.
    elif int(menu) == 5:
        value_per_item()

    # If the user selected "6" they can then view the heighest stocked item to be marked as for sale.
    elif int(menu) == 6:
        highest_qty()

    # If the user input is not reconized.
    else:
        print("Oops! You typed in a wrong input. Please try again.")