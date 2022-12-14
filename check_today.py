
import time
from rich import print

birthday_file = "list_of_birthdays.txt"

def checkbirthdays():
    birthdays = open(birthday_file, 'r')
    today = time.strftime('%m/%d')
    flag = 0
    # iterate through file, comparing date to current date
    for line in birthdays:
        if today in line:
            line = line.split(' ')
            flag =1
            # line[1] contains Name and line[2] contains Surname
            print("Remember to wish: [red]" + line[1] + ' ' + line[2] + ' ' "[/red]a very happy birthday!")
    
    if flag == 0:
        # message for if no birthdays matching today
        print("[italic green]Don't worry, you didn't forget anyone. There are no birthdays today.")
  
if __name__ == '__main__':
    checkbirthdays()