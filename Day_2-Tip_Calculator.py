print("Welcome to the tip calculator.")
t_bill = int(input("What was the total bill? "))
tip_p = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people split the bill? "))
tip = int(t_bill * tip_p) / (people * 100)
print(f"Each person should pay: {tip}")