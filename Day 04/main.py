import random

user_wins = 0
comp_wins = 0
options = ['rock','paper','scissors']

while True: # To make the game run in a loop untill quit.
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    
    random_num = random.randint(0,2) # This includes both 0 and 2
    # rock = 0, paper = 1, scissors = 2
    
    computer_pick = options[random_num]
    print("Computer picked",computer_pick + ".")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock ':
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie, no point.")

    else:
        print("You lost!")
        comp_wins += 1 

print("User won",user_wins,"times.")
print("Computer won",comp_wins,"times.")
print("GoodBye :)")
