#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10,12 or 15?"))
num_of_people = int(input("How many people to split the bill?"))
tip_amount = round(total_bill * tip_percentage / 100,2)
split_amount = (total_bill+tip_amount)/num_of_people
split_amount_two_digits = "{:.2f}".format(split_amount)
print(f"Each person should pay: ${split_amount_two_digits}")