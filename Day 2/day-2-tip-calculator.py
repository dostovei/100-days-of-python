#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# MY ATTEMPT BELOW
# print("Welcome to the tip calculator!")
# subtotal = float(input("What was the total bill?"))
# tip = input("What percentage tip would you like to give? 10, 12, or 15?")
# split = input("How many people to split the bill?")
# subtotal_float = float(subtotal)
# tip_int = int(tip) / 100
# split_int = int(split)
# total = (subtotal_float + (subtotal_float * tip_int)) / split_int
# print(f"Your payment will be {total}.")
#can't seem to get it to do 2 decimal places, but other than that I got it right.

#INSTRUCTOR SOLUTION CODED DIFFERENTLY
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person, 2) #This format function forces two decimal places even when it ends in a 0 ie $82.50, whereas round only returns $82.5
print(f"Each person should pay ${final_amount}")