import time
# import os

birthday_file = "list_of_birthdays.txt"

# month = input("Enter a month (01-12) to see the birthdays that month: ")

def check_a_month():
    month = input("Enter a month (01-12) to see the birthdays that month: ")
    birthdays = open(birthday_file, 'r')
    today = time.strftime('%m/%d')
    # month = time.strftime('%m') 
    flag = 0
    for line in birthdays:
        if  month in line[:2]:
            # line = line.split("/")
            flag =1
            print(line)  
    if flag == 0:
        print("There are no birthdays to remember that month.")
  
if __name__ == '__main__':
    check_a_month()