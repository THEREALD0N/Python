
#! Python calculator

operator = input ("Select your operator: (+, - , * , / ): ")

num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator" )