from datetime import date
import pandas as pd
import os   


#set current date 

today = date.today()
currentmonth = today.month
currentday = today.day

# message
def notification(Person):
    message = Person + """'s Birthday Today"""
    return message

df = pd.read_csv(r'birthdays.csv')

for i in range(len(df)):
    if df.loc[i, 'Month']==currentmonth and df.loc[i, 'Day'] ==currentday:
        birthdayperson = df.loc[i, 'Person']
    

# my_birthdays = open("birthdays.txt", "r")
# print(my_birthdays.readlines())




# my_birthdays.close()
