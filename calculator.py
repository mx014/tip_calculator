# Welcome user to the Tip Calculator.
print("Welcome to mx014's Tip Calculator.")
# Ask user for the total bill without tip, and store it in a variable,
# making the return type a float so they may type decimals.
bill = float(input("What was the total bill?\n$"))
# Ask user what percentage they'd like to tip and store it in a variable,
# making the return type 'int'.
tip_percentage = int(input("Enter what percentage tip you'd like to give.\n"))
# Ask user how many people they are splitting the bill with, storing it in a variable
# and making the return type 'int'.
people = int(input("How many people are you splitting the bill with?\n"))
# Set a new variable equal to 1.{tip_percentage}
tip = f"1.{tip_percentage}"
# Create a new variable and divide the total bill by the amount of people multiplied by the tip.
# Example: 100 / 5 * 1.12 = answer
pay = (float(bill) / int(people)) * float(tip)
# Print what each person should pay, using the round function to allow up to 2 decimal places.
print(f"Each person should pay ${round(pay, 2)}.")
