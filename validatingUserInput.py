
#! VALIDATE THE USER INPUT

# THE USERNAME CANT BE  LONGER THAN 16 CHARACTERS
#CANT HAVE SPACES
#CANT HAVE DIGITS
 

username = input("Enter your username: ")

if len (username) >16:
    print ("Your username is too long,\n it must be less than 16 characters")
elif " " in username:
    print ("Your username can't have spaces")
    #*Alternatively I couldve used the username.find(" ") 
    #* method to find the space and return -1 if it doesn't exist
elif not username.isalpha():
    print ("Your username can't have digits")