from os import system
from datetime import date
import time


# set date to use in main menu
today = date.today()
# set out the list of birthdays this is all drawn from
birthday_file = "list_of_birthdays.txt"

# Prints a menu with several options and returns the selected option
def print_options():
    # print(f'Welcome to your birthday reminder app. It is {today}. What would you like to do today?')
    print("1. Check for birthdays today")
    print("2. Check for birthdays in any given month")
    print("3. Add a birthday")
    print("4. Delete a birthday")
    print("5. Exit")
    opt = input("Select your option (1-5): ")
    return opt

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
        from check_today import *
        checkbirthdays()

    elif option == "2":
        from check_a_month import *
        check_a_month()
        
    elif option == "3":
        from Add_birthday import *
        add_birthday()
        
    elif option == "4":
        from delete_birthday import *
        remove_birthday()
       
    #manages the exit option and the invalid options
    elif option == "5":
        continue
    else:
        print("Invalid option")
    #adds a break in the control flow until the user presses Enter    
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 