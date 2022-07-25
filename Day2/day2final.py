# Tip Calculator takes in user input for final bill, desired
# tip, and number of people in party. Will output the amount each 
# should pay including tip

print("Welcome to the tip calculator.")
totalbill = float(input("What was the total bill? "))
tipPerc = int(input("What percentage tip would you like to give? 10, 15, 18, or 20? "))
numParty = int(input("How many people to split the bill? "))

tip = (tipPerc * .01) + 1
total = (totalbill * tip)

# another way:

# tip = tipPerc/100
# total = totalBill * tip 
# final = total + totalBill
# bill_per_person = final / numParty
# final_amount = round(bill_per_person, 2)
# Two decimal place format {:.2f}
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay ${final_amount})

each = round(total / numParty, 2)
print(f"Each person should pay: ${each}")
