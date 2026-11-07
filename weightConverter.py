

weight = float(input ("Enter your weight: "))
unit = input ("Enter your unit (KG or LB): ")

if unit == "KG":
    converted_weight = weight * 2.20462
    unit = "lbs"
elif unit == "LB":
    converted_weight = weight / 2.20462
    unit = "kgs"
else:
    print(f"{unit} is not a valid unit")
    exit()

print (f"Your weight is: {converted_weight:.2f} {unit}")