import random
from select import select
# Rock Paper Scissors
#How you will store the user's input.
#How you will generate a random choice for the computer.
#How you will compare the user's and the computer's choice to determine the winner (or a draw).
#And also how you will give feedback to the player.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Second way to solve with list implemntation
possibles = [rock, paper, scissors]

comp_num = random.randint(0,2)

selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if selection >= 3 or selection < 0:
    print("You typed an invalid number, you lose!")
else:
    print(possibles[selection])
    print(f"Computer chose: \n{possibles[comp_num]}")
    if selection == comp_num:
        print("It's a draw")
    elif (selection) == "0" and comp_num == 1:
        print("You lose")
    elif (selection) == "0" and comp_num == 2:
        print("You win!")
    elif (selection) == "1" and comp_num == 0:
        print("You win!")
    elif (selection) == "1" and comp_num == 2:
        print("You lose")
    elif (selection) == "2" and comp_num == 0:
            print("You lose")
    elif (selection) == "2" and comp_num == 1:
        print("You win!")
    else:
        print("an error occured - please try again")

#additional solution for determining win/loss
"""
if selection == "0" and comp_num == 2:
    print("You win!")
elif comp_num == 0 and selection == 2:
    print("You lose")
elif comp_num > selection:
    print("You lose")
elif selection > comp_num:
    print("You win!")
elif comp_num == selection:
    print("It's a draw") """


""" if selection == "0":
    print(rock)  
elif selection == "1":
    print(paper)
elif selection == "2":
    print(scissors)
else:
    print("Please try again with a valid selection (0-2)")

comp_num = random.randint(0,2)
if comp_num == 0:
    print(f"Computer chose: {rock}")
elif comp_num == 1:
    print(f"Computer chose: {paper}")
elif comp_num == 2:
    print(f"Computer chose: {scissors}")
print(comp_num)

if int(selection) == comp_num:
    print("It's a draw")
elif selection == "0" and comp_num == 1:
    print("You lose")
elif selection == "1" and comp_num == 0:
    print("You win!")
elif selection == "1" and comp_num == 2:
    print("You lose")
elif selection == "2" and comp_num == 0:
    print("You lose")
elif selection == "2" and comp_num == 1:
    print("You win!")
elif selection == "0" and comp_num == 2:
    print("You win!")
else:
    print("an error occurred") """




