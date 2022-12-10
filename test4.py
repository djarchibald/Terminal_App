
import time
birthday_file = "list_of_birthdays.txt"

def checkbirthdays():
    birthdays = open(birthday_file, 'r')
    today = time.strftime('%m/%d')
    
    for line in birthdays:
        if today in line:
            print("Make sure to wish a happy birthday to:")
            print(line[5:])
    
    else:
        if today not in line:
            print("Don't worry, you didn't forget anyone. There are no birthdays today.")
  
if __name__ == '__main__':
    checkbirthdays()