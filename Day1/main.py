# input will take in name
# then hello will be printed and the user input
print("Hello " + input("what is your name?"))

# input will take in user input of name
# then length of string of user input will be calculated
# then calculated length will be printed 
print(len(input("What is your name?")))

# same as above, but using variables to simplify
name = input("What is your name? ")
length = len(name)
print(length)


#take in "a" & "b" and returns flipped values 
# (with "b" as "a" & "a" as "b")
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

