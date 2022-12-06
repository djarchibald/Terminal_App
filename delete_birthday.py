birthday_list = open("birthdayformat.txt", "r")
for birthday in birthday_list.readlines():
    print(birthday)

to_delete = input("Your current list of birthdays is above. Please enter the birthday you wish to delete, in the exact format it appears in the list E.G. '1018 Duncan':   ")

with open("birthdayformat.txt", "r") as f:
    birthday_list = f.readlines()

with open("birthdayformat.txt", "w") as f:
    for line in birthday_list:
        if line.strip("\n") != (to_delete) :
            f.write(line)
print("Birthday deleted. Your list of birthdays is now:")

birthday_list = open("birthdayformat.txt", "r")
for birthday in birthday_list.readlines():
    print(birthday)
            
birthday_list.close()