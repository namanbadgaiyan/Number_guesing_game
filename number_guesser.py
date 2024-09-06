import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please enter a number greater then 0, Next Time!')
        quit()
else:
    print('Please enter a number, Next Time!')
    quit()
    
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number, Next Time!')
        continue
    
    if user_guess == random_number:
        print('Congratulation!, u guessed the number correct')
        break
    elif user_guess > random_number:
        print('u r above the number!')
    else:
        print('u r below the number')
print('U got it in', guesses, 'guesses')