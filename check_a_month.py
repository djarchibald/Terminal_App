import time
from rich import print

birthday_file = "list_of_birthdays.txt"

def check_a_month():
    # ask user to choose a month
    month = input("Enter a month (01-12) to see the birthdays that month: ")
    birthdays = open(birthday_file, 'r')
    today = time.strftime('%m/%d')
     
    flag = 0
    for line in birthdays:
        # only check first two digits of each line, representing the month.
        if  month in line[:2]:
            flag =1
            print(line)  
    if flag == 0:
        print("[yellow]There are no birthdays to remember that month.")
  
if __name__ == '__main__':
    check_a_month()
