#! python3
# Program to guess user's secret number

import time
print('Guess a number between 1 to 100!')
time.sleep(2)
low = 0
high = 100
response = ''
while response != 'c':
    guess = int((low + high)/2)
    print('Is your guess number %s?' %guess)
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' if the guess is too low. Enter 'c' to indicate the guess is correct.\n")
    if response == 'h' or response == 'l' or response == 'c':
        if response == 'h':
            high = guess
        else:
            low = guess
    else:
        print('Sorry, I did not understand your input')
        continue
print('Game over. Your guess number was: %s' %guess)
