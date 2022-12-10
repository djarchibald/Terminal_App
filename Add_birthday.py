def add_birthday():

    birthday_file = "list_of_birthdays.txt"


    birthday_file = open("list_of_birthdays.txt", "r")
    for birthday in birthday_file.readlines():
        print(birthday)

    birthday_file = open("list_of_birthdays.txt", "a")

    birthday_file.write(input("Your current list of birthdays is above. Please enter a new birthday in the format: MM/DD First Last. (Last name is optional).  E.G. 03/15 Santa Claus: ") + '\n')
    birthday_file.close()
    print("Birthday added. Your list of birthdays is now:")
    birthday_file = open("list_of_birthdays.txt", "r")

    for birthday in birthday_file.readlines():
        print(birthday)
        birthday_file.close()