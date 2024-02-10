#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to mx014's Tip Calculator.")
bill = input("What was the total bill?\n")
tip_percentage = input("Enter what percentage tip you'd like to give.\n")
people = input("How many people are you splitting the bill with?\n")

tip = f"1.{tip_percentage}"
pay = (float(bill) / int(people)) * float(tip)
print(f"Each person should pay ${round(pay, 2)}.")
