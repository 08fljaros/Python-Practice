# Castle Adventure Game
# Using If, else, elseif and assuring for case sensitvity with user input
# User chooses between different doors/keys to try to find the 'golden goblet'
# Like a choose your own adventure


print('''

                           ___,
                    o___.-' /
                    |      _\_
                    |___.-'   `
                    |
                    |
            _   _   j   _   _
           [_]_[_]_[_]_[_]_[_]
           [__j__j__j__j__j__]
             [_j__j__j__j__]
             [__j__j__j__j_]
             [_j__j/V\_j__j]
             [__j_// \\__j_]
             [_j__|   |_j__]
             [__j_|___|__j_]
             [_j__j__j__j__]
             [__j__j__j__j_]
  _   _   _  [_j__j__j__j__]  _   _   _   _
_[_]_[_]_[_]_[__j__j__j__j_]_[_]_[_]_[_]_[_]_
  _j__j__j__j[_j__j__j__j__]j__j__j__j__j_
     j  j  j [  j  j  j  j ] j  j  j  j    
''')
print("*****  Welcome to Castle Adventure Game  *****")
print("")
print("Your mission is to find the proper route to \nthe cellar that holds the Golden Goblet")
print("")
print("Be careful - some doors may be trap doors --\n if so, GAME OVER.")
print("")
print("The first area you entered has two doors available.")
print("One is a wooden door on the left and the right is a metal door")
first_choice = input("Which door do you choose? Left or Right (type 'left' or 'right') ")

first_lower = first_choice.lower()
if first_lower == 'left':
    print("You proceed forward into a lamp lit room")
    second_choice = input("There's a chipped red door and a green door.\n Which do you choose?\n (Type 'red' for red or 'green' for green) ")
    second_lower = second_choice.lower()
    if second_lower == 'red':
        print("The red door allows you to proceed further and find 3 keys inside that look like\n they would open a chest affixed to the wall")
        third_choice = input("One is brass , one is gold, and one is made of bronze\n Which do you choose?\n (Type 'brass' for brass key, 'gold' for the gold key, and 'bronze' for bronze) ")
        third_lower = third_choice.lower()
        if third_lower == 'brass':
            print("That was the right key!\n You found the Golden Goblet\n You've WON!")
        elif third_lower == 'gold':
            print("That key didn't open the chest. THe door has closed behind you. Your mission has failed.\n GAME OVER")
        elif third_lower =='bronze':
            print("That key didn't open the chest. The guards have now found you\n GAME OVER")
        else: 
            print("GAME OVER")
    else: 
        print("The green door opened up to the castle's guards!\n GAME OVER")
else: 
    print("Oh no! You found the trap door >_<\n GAME OVER")

