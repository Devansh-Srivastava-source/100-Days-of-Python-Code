import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','(',')','*','+']

n_letters = int(input("How many letters do you like in your password? "))
n_numbers = int(input("How many numbers do you like in your password? "))
n_symbols = int(input("How many symbols do you like in your password? "))

password_list = []

for char in range(n_letters):
    password_list.append(random.choice(letters))
for num in range(n_numbers):
    password_list.append(random.choice(numbers))
for sym in range(n_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)# this functions takes a list and shuffles all its elements

# To convert this list to string one method is to do by for loop.
# other method is given as:
print("".join(password_list))