print("Welcome to mx014's Tip Calculator.")
bill = float(input("What was the total bill?\n$"))
tip_percentage = int(input("Enter what percentage tip you'd like to give.\n"))
people = int(input("How many people are you splitting the bill with?\n"))

tip = f"1.{tip_percentage}"
pay = (float(bill) / int(people)) * float(tip)
print(f"Each person should pay ${round(pay, 2)}.")
