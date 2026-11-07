#First_name= "Anderson"
#Strings
#Full_name= "Anderson Tavares"
#Integers
#Age = 23
#Floats 
#Height = 1.800
#Booleans
#Is_Student = True
#if Is_Student:
    #print (f"Hey {Full_name},\n You're {Age} years old, \n You are {Height}cm tall, \n and you're a student in Python University.")
#else:
   # print (f"Looks like you're not a student, {Full_name}.")


#input function
# name = input("What's your name?  ")     
# age = int(input("How old are you?  "))
# print (f"Hello {name}, welcome to Python programming!") #* use a (F) string to include a variable in a string
# 

#! EXERCISE 1: CALCULCULATE THE AREA OF A RECTANGLE
# Length = float(input("Enter the length of the rectangle: "))
#Width = float(input("Enter the width of the rectangle: "))
#Area = Length * Width
#print (f"The area of the rectangle is: {Area} cm²")

#! EXERCISE 2: SHOPPING CART
#Item = input("What item are you buying?  ")
#price = float(input("What is the price of the item? £ "))
#quantity = int(input("How many items are you buying?  "))
#Total = price * quantity

#print (f"You are purchasing {quantity} {Item}(s)\nThe Total cost: £ {Total:.2f}")


#!IF STATEMENTS
#*only operates if the condition is true, if not it will skip the code block and move on to the next line of code 

#age = int(input ("Enter your age: "))12
#if age >= 18:
    #print ("You are old enough")
#else:
   #print ("You aren't old enough to open an account")

#! Logical Operators:
# and, or, not, THESE ARE USED TO COMBINE CONDITIONAL STATEMENTS
# AND - both conditions must be true
# OR - at least one condition must be true
#NOT - reverses the result, returns false if the result is true

#! conditional expressions:
#*conditional expressions are shortened code that uses the 
#*if else statement to return a value based on a condition
#age = int(input ("Enter your age: "))
##status = "Adult" if age >= 18 else "You is a minor"
#if status == "Adult":
    #print (f"You are a {status}")
#else:
    #print (f"I hate to tell you, but {status}")

#! exercise 3: NAME LENGTH 
#name = input ("What your name? : ")

#length =len(name)
#find = name.find("a").upper()
#if name == "":
#print ("You didn't enter a name")
#else:
    #*print (f"Hey {name}, your name has {length} characters in it")