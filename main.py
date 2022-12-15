from os import system
from datetime import date
import time
from sys import argv
from rich import print
# from rich.prompt import prompt


guidance = "help.txt"


# set date
today = date.today()
# set out the list of birthdays this is all drawn from
birthday_file = "list_of_birthdays.txt"

# Prints a menu with several options and returns the selected option
def print_options():
    
    print("1. Check for birthdays today")
    print("2. Check for birthdays in any given month")
    print("3. Add a birthday")
    print("4. Delete a birthday")
    print("5. Help")
    print("6. Exit")
    print('')
    opt = input("Select your option (1-6): ")
    return opt

option = ""

# Menu: while loop prints the menu option and the user select the option.
# loop only stops when the input is 6 (exit option)

while option != "6":
    system('clear')
    print(f"[italic yellow]Welcome to your birthday reminder app. It is {today}. What would you like to do today?")
    print('')
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
    # help options:
    elif option == "5":
        guidance_file = "help.txt"
        guidance_file = open("help.txt", "r")
        print(guidance_file.read())
        guidance_file.close()

   
    elif option == "6":
        continue
    # error control:
    else:
        print("[red]Invalid option")
    #adds a break in the control flow until the user presses Enter:    
    input("press Enter to continue...")
    system('clear')

print("[yellow]Goodbye!") 