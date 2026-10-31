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
#// name = input("What's your name?  ")     
#// age = int(input("How old are you?  "))
#// print (f"Hello {name}, welcome to Python programming!") #* use a (F) string to include a variable in a string
#// 

#! EXERCISE 1: CALCULCULATE THE AREA OF A RECTANGLE

#// Length = float(input("Enter the length of the rectangle: "))
#//Width = float(input("Enter the width of the rectangle: "))
#//Area = Length * Width
#//print (f"The area of the rectangle is: {Area} cm²")

#! EXERCISE 2: SHOPPING CART

#//Item = input("What item are you buying?  ")
#//price = float(input("What is the price of the item? £ "))
#//quantity = int(input("How many items are you buying?  "))
#//Total = price * quantity

#//print (f"You are purchasing {quantity} {Item}(s)\nThe Total cost: £ {Total:.2f}")


#! MADLIBS GAME
print ("Welcome to the Madlibs game!")
name = input("Enter a name:")
place = input("Enter the name of a place:")
adjective = input("Enter an adjective:")
noun = input("Enter a noun:(place, person, animal, or thing): ")
name2 = input("Enter another name:")

print (f"One day, {name} went to {place}.\nIt was a very {adjective} day.\nSuddenly, a {noun} appeared and scared {name2}.")

