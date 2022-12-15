# Coder Academy, T1A3: Terminal Application. Duncan Archibald  

**Link to Github repo:** https://github.com/djarchibald/Terminal_App
** Link to youtube presentation: https://youtu.be/TSpqt8Exeu4


## Features
- **Executable**  
  This app is executable from the command line, and does not require the user to have a working knowledge of python. Upon opening, the app will automatically check to see that python is installed onthe user's machine - if yes, the app will open. If no, the user will be directed to download the latest version of python from their website. 

  The bash script is saved in a file: ./happybirthday.sh. To open in Terminal CD to the app files and type: ./happybirthday.sh
    
- **Main Menu**  
  Function is ```print_options()```.  

  The home page/main menu plays a key role in managing the flow of the app. It is the first thing the user sees when using the app, and is the page to which they are returned when their selected option is complete.  
  
  The menu is intended to be clear and straightforward, allowing the user to navigate easily to their desired option. It has brief, clear instructions but should the user inadvertently enter an invalid option (any chaaracter other than the numbers 1-6), the app will notfiy the user that they have entered something incorrectly before returning them to the main menu to try again.

  To achieve this, I used a while loop (combined with a number of if-else and elif statements), which is broken when only when the user selects the exit option. Each option listed to the user then invokes the relevent function, or in the case of accessing the help file, opens, reads and prints the detailed guidance for the user. 
  

- **Check today's date**  
  Function is ```checkbirthdays()```.  
  This function is designed to automatically check the list of birthdays against today's date. If a match is found, the user is reminded to wish that person/those people a happy birthday. If no match is found the app reassures the user they have not forgotten a birthday and confirms that there are non listed today. 

  Beyond selecting the option from the main menu, user input into this feature is not required. To achieve this I made use of a for loop, which iterates thorugh each line in the list of birthdays. I used a flag variable with if statements, which when true (==0 in the code) returns a message that there are no birthdays today. If false (i.e. flag == 1 in the code) it means there is a birthday matching the date. The app then prints the name(s) of whoever the user needs to wish a happy birthday to. As mentioned above, the user is returned to the main menu once the app has printed either of the two message options. 



- **Check a user defined month**  
  Function is ```check_a_month()```.  

  When originally conceived, I had intended that this option would allow users to check for birthdays in a given range from two dates that they had entered. My coding limitations meant I wasn't able to implement it in a way that I was happy with (i.e. that worked consistently) within the timeframe I had available and so opted to change it to allow the user to check a given month instead. While a fall-back option, the practical outcome for the user is similar to that which I had originally intended - they can see any birthdays for a month they select and if wish to see mutliple months are able with just a few inputs run the app as many times as they like to cover the months of interest.  

  Unlike the previous function, this one does require user input, with the user prompted to enter a number from 01-12 to select the month they wish to check. I used a for loop and if statements to allow the function to iterate through the list of birthdays checking only the first two characters (i.e. the month) of each line. Any matches are then printed for the user (thus listing all the birthdays for the selected month). If there are no matches, the user is given a message that there are no birthdays that month. After either message is printed, the user is prompted to hit enter to return to the main menu. 

- **Add birthday**  
  Function is ```add_birthday()```.  

  This option, allows the user to add a birthday to the database that the app checks in options 1 and 2. This function makes use of a couple of for loops to firstly display the list of birthdays as it stands, and then, following the user input, to display the newly amended list (to confirm the new data has been enetered correctly.  
  
   On selecting option 3, the app accesses the birthday list in read mode, and prints it for the user. The code then closes the file and reopens it in append mode. The user is prompted to enter the new birthday they wish to save, which is written to the next line in the list. The second loop then runs, iterating through the list, and printing all the entries. This allows the user to confirm they have sucesfully entered a new birthday, before being prompted to hit enter to return to the main menu.

- **Remove birthday**  
  Function is ```remove_birthday()```.  

  This option allows users to delete a birthday that they no longer wish to be reminded about. It also serves as a method for removing any incorrectly entered data.  

  On selecting this option, the app accesses the birthday list in read mode, and prints the complete list. The user is prompted to enter the data they wish to delete. The function makes use of for loops, with if statements to determine if the data entred matches (or not) a line in the list. with  With the birthday list open in write mode, the app loops through the list, looking for any data that matches user the user input, and writes any that don't match (i.e. generating a list without the entry that the user wants deleted). The user is shown a message that the birthday they entered has been deleted, alongside a printout (at this point the app accesses the list in read mode) of the new list (i.e. less the data the user inputed earlier).  

  This option can also be used to remove data that has been entered in error, or in the incorrect format from the list.


## Implementation Plan

**Selection of Trello board screenshots**  
Covering creating basic implementation plan through to near completion (still need to upload presentation & submit at time of writing)  

**Overview**
![Screenshot Trello board overview](trello%20images/trello%20board%20overview.jpeg)  

**First Steps**
![screenshot of trello board basic implementation plan](trello%20images/Trello%20Board%20-%20%20basics%20to%20do%20list.jpeg)  

**Python**
![screenshot of trello board python coding to-do list](trello%20images/Trello%20board%20-%20python%20coding%20to%20do%20list.jpeg)  

**Bash scripting**
![screenshot of trello board bash scripting to do list](trello%20images/trello%20board%20bash%20scripting%20to%20do%20list.jpeg)  

**Nearly complete:**
![trello board showing all actions done except upload](trello%20images/Trello%20board%20-%20complete%20(except%20upload).jpeg)


## Help
Help documentation can be found under option 5 in main menu of the app (or ./help.txt, if prefer)
