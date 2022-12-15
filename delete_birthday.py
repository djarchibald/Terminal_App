def remove_birthday():
    # print current birthday list for user
    birthday_list = open("list_of_birthdays.txt", "r")
    for birthday in birthday_list.readlines():
        print(birthday)
    # get user input on which birthday to delete
    to_delete = input("Your current list of birthdays is above. Please enter the birthday you wish to delete, in the exact format it appears in the list E.G. '10/18 Duncan Archibald': ")
    with open("list_of_birthdays.txt", "r") as f:
        birthday_list = f.readlines()
    # iterate through looking for line that matches user input & print any that don't match
    with open("list_of_birthdays.txt", "w") as f:
        for line in birthday_list:
            if line.strip("\n") != (to_delete) :
                f.write(line)
    print("[yellow]Birthday deleted. Your list of birthdays is now:")
    # print new list of birthdays for the user to confirm data removed.
    birthday_list = open("list_of_birthdays.txt", "r")
    for birthday in birthday_list.readlines():
        print(birthday)
            
    birthday_list.close()