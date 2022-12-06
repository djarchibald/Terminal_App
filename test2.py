import time
import os

birthday_file = birthdayformat.txt

def checkTodaysBirthdays():
    fileName = open("birthdayformat.txt", 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
            # line[1] contains Name and line[2] contains Surname
            # os.system('notify-send "Birthdays Today: ' + line[1]
            # + ' ' + line[2] + '"')
    if flag == 0:
        print("no birthdays today")
if__name__ == '__main__'
print("happy birthday")