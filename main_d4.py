import random

# Virtual coin toss game
# User guesses heads or tails and dice rolls 
# should correct input if user enters 'heads' vs 'Heads'

user_select = input("Will it be heads or tails?").capitalize()

random_result = random.randint(0,1)

if random_result == 0:
    print("Tails")
    if user_select == "Tails":
        print("Your luck is strong!")
    else:
        print("Better luck next time")
else:
    print("Heads")
    if user_select == "Heads":
        print("Your luck is strong!")
    else:
        print("Better luck next time")


# Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "New Mexico"]
print(states_of_america[2])



# 'Who will pay the bill?' program
names_string = input("Give me the names of everyone in the party, separated by a comma")
#splits string into a list with comma separation parameter
names = names_string.split(', ')

#obtains number of elements in list
number_in_party = len(names)
#picks random int based on number in party
# -1 added as index starts at 0 for list, otherwise it is neglecting 1st element
random_num = (random.randint(0, number_in_party-1))
print(f"{names[random_num]} is going to buy the meal today!")


##list of lists and grabbing an element within
#dirty_dozen_list = ["strawberries", "spinach", "kale", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])

##lists, continued
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#backward indexing
print(fruits[-1])
#adding an element to the end of a list
fruits.append("lemons")
print(fruits)


#Treasure Map program
# Takes in user input to mark a spot on the "map"

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


num_list = [int(digit) for digit in str(position)]
print(num_list)
column = num_list[0]
row = num_list[1]
if row == 1:
    if column == 1:
        row1 = ["X","⬜️","⬜️"]
    elif column == 2:
        row1 = ["⬜️","X","⬜️"]
    elif column == 3:
        row1 = ["⬜️","⬜️","X"]
    else:
        print("Error- Choose a valid option")
elif row == 2:
    if column == 1:
        row2 = ["X","⬜️","⬜️"]
    elif column == 2:
        row2 = ["⬜️","X","⬜️"]
    elif column == 3:
        row2 = ["⬜️","⬜️","X"]
    else:
        print("Error- Choose a valid option")
elif row == 3:
    if column == 1:
        row3 = ["X","⬜️","⬜️"]
    elif column == 2:
        row3 = ["⬜️","X","⬜️"]
    elif column == 3:
        row3 = ["⬜️","⬜️","X"]
    else:
        print("Error- Choose a valid option")
else:
    print("Invalid entry - try again")
    

print(f"{row1}\n{row2}\n{row3}")
