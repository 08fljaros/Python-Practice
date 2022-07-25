# finds the requested index of the container/string
#print("Hello"[0])

#Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
str_nums = str(two_digit_number)
num1 = str_nums[0]
num2 = str_nums[1]
sum = int(num1) + int(num2)
print(sum) 

# BMI Calculator Exercise
# Takes in 2 user inputs and returns bmi as a whole number
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h= float(height)
w = float(weight)
bmi = w/h**2
print(int(bmi))

# Time Left Calculator (if you live until 90)

age = input("What is your current age?")
yourAge = int(age)
years = 90 - yourAge
months = 12 * years
weeks = 52 * years
days = 365 * years
print(f"You have {days} days, {weeks} weeks, and {months} months left")
