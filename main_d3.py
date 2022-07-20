# DAY 3
# if-else statements
# nested if and elif
# Takes in height and age via user input
# guests uder 12 pay $5, between 12-18 pays $7 and over 18 pays $12
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height >120:
    print("You are tall enough for this ride")
    age = input("What is your age? ")
    if age < 12:
        print("Please pay $5")
    elif age >=12 & age <= 18:
        print("Please pay $7")
    else: 
        print("Please pay $12")
else:
    print("Sorry, you will have to grow taller to ride")




# odd or even - modulo
number = int(input("Which number do you want to check? "))
if number % 2 == 0:     
    print("This is an even number.")
else: 
    print("This is an odd number.")



#bmi 2.0 - Characterization of obesity based on bmi range
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/height**2
roundB = int(round(bmi))

if roundB < 18.5:
    message = "you are underweight."
elif roundB <25:
    message = "you have a normal weight."
elif roundB <30:
    message = "you are slightly overweight."
elif roundB <35: 
    message = "you are obese."
else: 
    message = "you are clinically obese."

print(f"Your BMI is {roundB}, {message}")


#has user enter in a year to see if it is a leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 != 0:
        print("leap year")
    else:  
        if year % 400 == 0:
            print("leap year")
        else: 
            print("not leap year")           
else: 
    print("Not leap year")


# multiple if statements - continuing the rollercoaster example
# logical operators
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
ticket = 0


if height >120:
    print("You are tall enough for this ride")
    age = input("What is your age? ")
    if age < 12:
        ticket= 5
        print("Child tickets are $5")
    elif age >=12 and age <= 18:
        ticket = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Your ticket is free - you get the midlife crisis discount (:")
    else: 
        ticket = 12
        print("Adult tickets are $12")
    photoWanted = input("Would you like photos of your ride? enter 'yes' if yes and 'no' if no")
    if photoWanted == 'yes':
        ticket +=3
    print(f"The total bill is ${ticket}")
else:
    print("Sorry, you will have to grow taller to ride")

# Pizza order program
# Find total price based on user selection of size and topping options

print("Welcome to Python Pizza Deliveries!")
print("Here is our menu:")
print("Small Pizza - $15")
print("Medium Pizza - $20")
print("Large Pizza - $25")
print("")
print("Pepperoni for Small Pizzas - +$2")
print("Pepperoni for Medium or Large Pizzas - + $3")
print("")
print("Extra cheese for any size pizza - +$1")
print("")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0

if size == "L":
    price +=25
elif size == "M":
    price +=20
elif size == "S":
    price += 15
if add_pepperoni == "Y":
    if size == "S":
        price +=2
    else:
        price +=3
if extra_cheese == "Y":
    price += 1   
else:
    print("Choose a valid size: S, M, or, L")
print(f"The total price for your pizza is: ${price}")

#Love Calculator
# Takes in user input of two names, lowers the case,
# checks count of number of the letters or "True love" in both names provided
# returns compatibility score based on number of letters found

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

name_L = name1_lower.count("l") + name2_lower.count("l")

name_O = name1_lower.count("o") + name2_lower.count("o")

name_V = name1_lower.count("v") + name2_lower.count("v")

name_E = name1_lower.count("e") + name2_lower.count("e")

total_love = name_L + name_O + name_V + name_E


name_T = name1_lower.count("t") + name2_lower.count("t")

name_R = name1_lower.count("r") + name2_lower.count("r")

name_U = name1_lower.count("u") + name2_lower.count("u")

name_e = name1_lower.count("e") + name2_lower.count("e")

total_true = name_T + name_R + name_U + name_e


total_score = int(str(total_true) + str(total_love))

if total_score <= 10 :
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 90 : 
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50: 
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")