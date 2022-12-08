birthday_list = "list_of_birthdays.txt"


birthday_list = open("list_of_birthdays.txt", "r")
for birthday in birthday_list.readlines():
    print(birthday)

birthday_list = open("list_of_birthdays.txt", "a")

birthday_list.write(input("Your current list of birthdays is above. Please enter a new birthday in the format: MM/DD First Name e.g. 1018 Duncan: ") + '\n')
birthday_list.close()
print("Birthday added. Your list of birthdays is now:")
birthday_list = open("list_of_birthdays.txt", "r")

for birthday in birthday_list.readlines():
    print(birthday)
    birthday_list.close()