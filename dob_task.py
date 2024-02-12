# This program reads the contents of file DOB.txt and prints the name and date of birth details from
# the file separately
# While running the example code in Visual Studio Code found though my text file was in same directory it 
# was not fetching or identifying it and got No such file or directory error. I quickly researched
# online and found the setting which needed to be changed to fix this issue. Referred links are below:
# https://bryansiegel.com/2020/04/how-to-fix-visual-studio-codes-run-python-in-file-directory-for-opening-files/
#https://stackoverflow.com/questions/53900141/how-to-run-python-interactive-in-current-files-directory-in-visual-studio-code

name = [] # Set name as a list to hold all names from the file
dob = [] # Set dob as a list to hold all date of birth from the file
contents = "" # Set contents as empty string

with open('DOB.txt','r') as file: # Open file DOB.txt in read mode
          lines = file.readlines() # Read each line of the file into lines list

# Loop through lines list and get each line and split without any parameter so the contents of the 
# line are split based on spaces. So contents now has first name as first element, last name as second
# element, birthdate as third, month as fourth and year as fifth element after the split

for line in lines:
    contents = line.split()
    name.append(" ".join(contents[:2]))   # Append firstname, lastname to name list  
    dob.append(" ".join(contents[2:5])) # Append date, month and year to dob list 

if (len(name) > 0): # Check if names exists in the name list
    print("Name:\n") 
    for i in range(len(name)):
           print(name[i]) # Print name and loop through name list and print all names.

if (len(dob) > 0): # Check if birth date exists in the dob list
       print("\nBirthdate:\n")
       for i in range(len(dob)): # loop through dob list
              print(dob[i]) #print all date of births

if (len(name) == 0 and len(dob) == 0): #check if name and dob list are empty 
       print("No records found in file to display") #print no records found
