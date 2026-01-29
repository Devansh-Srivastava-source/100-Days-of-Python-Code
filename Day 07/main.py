import random

STAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ['aadvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print("Welcome to the Hangman game")
for i in range(word_length):
    print("_ ",end="")

correct_letters = []
game_over = False
lives = 6 # determines how many times user can go wrong

while not game_over:
    flag = False
    guess = input("\nGuess a letter: ").lower()
    display = ""
    
    for letter in chosen_word: 
        if letter == guess:
            display += letter+" "
            correct_letters.append(guess)
            flag = True
        elif letter in correct_letters:
            display += letter+" "
        else:
            display += "_ "
        
    if flag == False:
        lives -= 1
    if lives == 0:
        game_over = True
        print("\nYOU LOST THE GAME.")

    print(STAGES[6-lives]) # Prints the stages of hangman.

    print(display) # This will occur after every loop to know whether user is correct or not

    if '_' not in display:
        game_over = True
        print("\nYou won!")
    
    