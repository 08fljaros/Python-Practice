from random import shuffle
from random import sample
from random import choice
# Password Generator

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["@", "!", "#", "$", "%", "^", "*", "(", ")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the Password Generator")
ui_letters = int(input("How many letters would you like in your password? \n"))
ui_symbols = int(input("How many symbols would you like in your password? \n"))
ui_numbers = int(input("How many numbers would you like in your password? \n"))
total = ui_letters + ui_symbols + ui_numbers

pswd_letters = []
pswd_symbols = []
pswd_num = []
mix = []

for n in range(0, ui_letters):
    pswd_letters.append(choice(letters))
for n in range(0, ui_symbols):
    pswd_symbols.append(choice(symbols))
for n in range(0, ui_numbers):
    pswd_num.append(choice(numbers))
    

pswd = pswd_letters + pswd_symbols + pswd_num


print(f"Total length of password is: {total} characters")
#pswd is easy level - in sequence vs all elements being completely random


# hard level - randomize easy answer

#create copy of pswd and store in new1
new1 = pswd[:]
shuffle(new1)

print(type(new1))
print(f"Your new password is: {new1}")

#alt way to shuffle

""" new2 = sample(pswd, len(pswd))
print(new2) """

#convert list of characters to string
new4 = ''.join(new1)
print(new4)