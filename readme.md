# Coder Academy, Term 1 Assignment 3: Terminal Application. Duncan Archibald  

**Link to Github repo:** https://github.com/djarchibald/Terminal_App

## Features
- **Executable**  
  This app is executable from the command line, and does not require the user to have a working knowledge of python. Upon opening, the app will automatically check to see that python is installed onthe user's machine - if yes, the app will open. If no, the user will be directed to download the latest version of python from their website. 
    
- **Main Menu**  
  The home page/main menu plays a key role in managing the flow of the app. It is the first thing the user sees when using the app, and is the page to which they are returned when their selected option is complete.  
  
  The menu is intended to be clear and straightforward, allowing the user to navigate easily to their desired option. It has brief, clear instructions but should the user inadvertently enter an invalid option, the app will notfiy the user that they have entered something incorrectly before returning them to the main menu to try again.

  To achieve this, I used a while loop which is broken when only when the user selects the exit option. Each option listed to the user then invokes the relevent function, or in the case of accessing the help file, opens, reads and prints the detailed guidance for the user. 
  

- **Check today's date**  
  Function is ```checkbirthdays()```.  
  This function is designed to automatically check the list of birthdays against today's date. If a match is found, the user is reminded to wish that person/those people a happy birthday. If no match is found the app reassures the user they have not forgotten a birthday and confirms that there are non listed today. 

  Beyond selecting the option from the main menu, user input into this feature is not required. To achieve this I made use of a for loop, which iterates thorugh each line in the list of birthdays. I used a flag variable, which when true (==0 in the code) returns a message that there are no birthdays today. If false (i.e. flag == 1 in the code) it means there is a birthday matching the date. The app then prints the name(s) of whoever the user needs to wish a happy birthday to. As mentioned above, the user is returned to the main menu once the app has printed either of the two message options. 



- **Check a user defined month**  
  Function is ```check_a_month()```.  

  When originally conceived, I had intended that this option would allow users to check for birthdays in a given range from two dates that they had entered. My coding limitations meant I wasn't able to implement it in a way that I was happy with (i.e. that worked consistently) within the timeframe I had available and so opted to change it to allow the user to check a given month instead. While a fall-back option, the practical outcome for the user is similar to that which I had originally intended - they can see any birthdays for a month they select and if wish to see mutliple months are able with just a few inputs run the app as many times as they like to cover the months of interest.  

  Unlike the previous function, this one does require user input, with the user prompted to enter a number from 01-12 to select the month they wish to check. The function then loops through the list of birthdays checking only the first two characters (i.e. the month) of each line. Any matches are then printed for the user. If there are no matches, the user is given a message that there are no birthdays that month. After either message is printed, the user is prompted to hit enter to return to the main menu. 

**Add birthday**

**Remove birthday**

## Implementation Plan

## Help
Help documentation can be found under option 5 in main menu of the app (or ./help.txt, if prefer)
