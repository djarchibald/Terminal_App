import time
# import os
birthday_file = "birthdayformat.txt"

def checkbirthdays():
    birthdays = open(birthday_file, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in birthdays:
        if today in line:
            line = line.split(' ')
            flag =1
            # line[1] contains Name and line[2] contains Surname
            print("Remember to wish: " + line[1] + ' ' + line[2] + ' ' "a happy birthday!")
    if flag == 0:
            # os.system('notify-send "No Birthdays Today!"')
            print("Don't worry, you didn't forget anyone - there are no birthdays today.")
  
if __name__ == '__main__':
    checkbirthdays()