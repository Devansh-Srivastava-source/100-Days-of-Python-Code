print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at a crossroad, where do you want to go? (left/right)').lower()
# .lower() converts into lowercase
if choice1 == "left":
    choice2 = input("You\'ve come accross a lake. Will you wait for a boat or swim " \
    "around? (wait/swim)").lower()
    # It is advised by PEP guidelines, to not write too much in a line
    if choice2 == "wait":
        choice3 = input("You arrived the island unharmed, now there are three doors" \
        "infront you you. Red, Blue, Yellow. What would you choose? ").lower()
        
        if choice3 == "red":
            print("Room is full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure. You win!")
        elif choice3 == "blue":
            print("The room is full of beasts. Game over.")
        else:
            print("Your choice is invalid. Game over.")
        
    else:
        print("You got attacked by an angry trout. Game over.")
        

else:
    print("You fell into a hole. Game over.")