from os import system
from datetime import date
# from seed import seed
# from items_operations import print_list_of_items, add_item, delete_item, update_item_price

#gets the list of products from the seed method, imported from seed.py
# list_of_products = seed()

# define today
today = date.today()


# Prints a menu with several options and returns the selected option
def print_options():
    # print(f'Welcome to your birthday reminder app. It is {today}. What would you like to do today?')
    print("1. Check for birthdays")
    print("2. Check for birthdays in a given period")
    print("3. Add a birthday")
    print("4. Delete a birthday")
    print("5. Exit")
    opt = input("Select your option (1-5): ")
    return opt


# def birthday_checker():
#     # asks for name and
    
    

#     # add_item(list_of_products, name, price)
#     # print(f"{name} being added to the menu...")
    


# def range_checker():
#     #show the list of products
#     # print_list_of_items(list_of_products)
#     #ask about the product we want to delete
#     name = input("What is the product you want to delete? ")
#     # delete_item(list_of_products, name)
#     #make sure it is in the menu

#     #delete it

# def add_birthday():
#     #show the list of products
#     # print_list_of_items(list_of_products)
#     #ask about the product we want to delete
#     name = input("What is the product you want to update? ")
#     #make sure it is in the menu
#     # update_item_price(list_of_products,name)
#     #ask for the new price

# def delete_birthday():
#     print("start a new order...")
#     # under construction

option = ""

# Menu feature: The while loop prints the menu option and the user select the option.
# Each valid option invokes the selected function
# The loop only stops when the input is 6 (exit option)

while option != "5":
    system('clear')
    print(f'Welcome to your birthday reminder app. It is {today}. What would you like to do today?')
    
    # invoke print options and return the selected option
    option = print_options()
    system('clear')
    if option == "1":
        print("Will check for birthdays today...")
        
    elif option == "2":
        print("asks user to set date range and checks for birthdays in that range")
        
    elif option == "3":
        print("allows user to add a birthday")
        
    elif option == "4":
        print("allows user to delete a birthday")
       
    #manages the exit option and the invalid options
    elif option == "5":
        continue
    else:
        print("Invalid option")
    #adds a break in the control flow until the user presses Enter    
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 