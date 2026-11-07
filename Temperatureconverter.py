
Temperature = float(input("ENTER THE TEMPERATURE: "))
unit = input("Enter the Unit (C or F): ").upper()

if unit == "C":
    converted_temperature = (Temperature * 9/5) + 32
    unit = "Fahrenheit"
elif unit == "F":
    converted_temperature = (Temperature - 32) * 5/9
    unit ="Celsius"
else:
    print(f"{unit} is not a valid unit")
    exit()

print(f"Your temperature is: {converted_temperature:.2f} {unit}")