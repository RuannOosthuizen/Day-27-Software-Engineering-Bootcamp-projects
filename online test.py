#T32 - CAPSTONE IV - OOP

####   CLASS DEFINITION   ####

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
    
    def __str__(self):
        return f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}"

####   FUNCTIONS DEFINITION   ####

#FILE READ INTO A STOCK LIST
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as list:
            next(list)
            for line in list:
                line = line.strip().split(',')
                shoes_list.append(Shoes(line[0], line[1], line[2], float(line[3]), int(line[4])))
    except FileNotFoundError:
        print('File not found. Assure the inventory.txt is available in the folder and start again.')

#APPEND STOCK LIST WITH NEW ENTRY
def capture_shoes():
    country = input('Enter country: ')
    code = input('Enter code: ')
    product = input('Enter product name: ')
    
    while True:
        cost = input('Enter cost: ')
        try:
            float(cost)
            cost = float(cost)
            break
        except:
            print('\n Incorrect input, try again!\n')

    while True:
        quantity = input('Enter quantity: ')
        if quantity.isnumeric():
            quantity = int(quantity)
            break
        else:
            print('\n Incorrect input, try again!\n')
    
    shoes_list.append(Shoes(country, code, product, cost, quantity))
    print('Shoes added successfully!')

#DISPLAY THE LIST
def view_all():
    headers = ['Position', 'Country', 'Code', 'Product', 'Cost', 'Quantity']
    print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<10}".format(*headers))
    for pos in shoes_list:
        print('{:^10} {:<20} {:<10} {:<20} {:<10.2f} {:^10}'.format(shoes_list.index(pos)+1, pos.country, pos.code, pos.product, pos.cost, pos.quantity))

#FIND THE LEAST STOCKED ITEM AND PROMPT FOR RESTOCK
#IF RESTOCKED - REWRITES THE TXT FILE
def re_stock():
    min_qty = min(pos.quantity for pos in shoes_list)
    for pos in shoes_list:
        if pos.quantity == min_qty:                                                             #This will return the first low stock item in the list. Requires further work to show all low stock items.
            print(f'{pos.product} is low stock! {pos.quantity} pairs left')
            while True:
                choice = input('Do you want to order more? Type y - yes or n - no: ').lower()
                if choice == 'y':
                    while True:
                        qty_to_add = input("Enter quantity to add: ")
                        if qty_to_add.isnumeric():
                            qty_to_add = int(qty_to_add)
                            break
                        else:
                            print('Wrong input, try again!')
                    pos.quantity += qty_to_add
                    with open('inventory.txt', 'r') as list:
                        lines = list.readlines()
                    with open('inventory.txt', 'w') as list:
                        lines[shoes_list.index(pos)+1] = f"{pos.country},{pos.code},{pos.product},{pos.cost},{pos.quantity}\n"
                        list.writelines(lines)
                    print('STOCK UPDATED')
                    break
                if choice == 'n':
                    print('STOCK NOT CHANGED')
                    return
                else:
                    print('Invalid input, try again!')
                    continue

#SHOE SEARCH PER CODE
def search_shoe():
    code = input('Enter code: ')
    for pos in shoes_list:
        if pos.code == code:
            print(pos)
            return
    print("Position not found, assure correct input!")

#STOCK VALUE PER ITEM
def value_per_item():
    print('\nSTOCK VALUE PER ITEM LIST\n')
    for pos in shoes_list:
        print(f'{shoes_list.index(pos)+1} {pos.product} - Total value: {pos.cost*pos.quantity}')

#HIGH QUANTITY ITEM FOR SALE
def highest_qty():
    max_qty = max(pos.quantity for pos in shoes_list)
    for pos in shoes_list:
        if pos.quantity == max_qty:
            print(f"We have too much of {pos.product} at ({pos.quantity}). Put on sale!")
            return

####   VARIABLES AND MAIN BODY   ####

shoes_list = []

print('''
    ####    STOCK TAKE    ####
    Welcome to the stock take program.
    This program allows you to view and modify your inventory
''')

read_shoes_data()


#MENU
while True:
    print('''
    SELECT AN OPTION
    1. VIEW INVENTORY
    2. ADD AN ITEM
    3. CHECK LOW STOCK ITEM
    4. CHECK STOCK BY CODE
    5. CHECK STOCK VALUE PER ITEM
    6. WHATS FOR SALE
    7. EXIT
    ''')

    choice = input('What is your choice: ')
    if choice == '1':
        view_all()
    elif choice == '2':
        capture_shoes()
    elif choice == '3':
        re_stock()
    elif choice == '4':
        search_shoe()
    elif choice == '5':
        value_per_item()
    elif choice == '6':
        highest_qty()
    elif choice == '7':
        print('TOODLE-OO!')
        break        
    else:
        print('Invalid choice, please try again.')