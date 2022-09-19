# Defining functions



#Basic function 
name = input("What is your name? ")
def printing():
    print(f"Hello {name}")

printing()
##


#function with an arg

def your_name(f_name):
    print(f"{f_name} is a great name")

your_name("Marie")
your_name("Julie")

##

#When you don't how many args to accept
# add a '*' before param/arg name

def youngest(*kids):
    print(f"The youngest child is: {kids[2]}")

youngest('Emilio', 'Roberto', 'Ferdinand')
##

#Arbitrary keyword arguments (kwargs)
#For when you're uncertain the # of kwargs to accept

def another(**kid):
    print(f"Here is the child's last name:" + kid["f_name"])
another(f_name="Angela", l_name="Ronning")
##

#Default parameter value -- if calling the function without argument

def another_function(fruit = 'apple'):
    print("My favorite fruit is " + fruit)
another_function("grape")
another_function("orange")
another_function()
another_function("melon")
##


## Passing a list as an argument - type remains as it passes through function

def my_function(food):
    for x in food: 
        print(x)
veggies = ['tomato', 'kale', 'zucchini', 'corn', 'broccoli']
my_function(veggies)



fruit = ['apples', 'bananas', 'grapes', 'lemons']


def find_the_third(food):
    print("Here is the 3rd fruit: "+ food[2])
find_the_third(fruit)
##


# Returning values with a function

def five_multiply(x):
    return 5 * x

print(five_multiply(4))
print(five_multiply(3))
print(five_multiply(2))
##


# For functions without content, add pass

def blank():
    pass
##

#division

print ('floor divison:', 8//3)
print('modulo: ', 8%3)

# While loops

scores = (input("Enter a list of scores separated by spaces"))
listed = scores.split()
new = list(map(int,listed))

count = 0
sum = 0

while count < len(new):
    
    for i in new:  
        sum += i
        count+=1
print(f"The sum of the scores you entered is: {sum}")