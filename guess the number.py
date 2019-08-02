#guess the number

'''
Generate a random number and have the user guess the number. If the user is wrong, return 
an indication of how wrong - "too high" or "too low". If the user guesses correctly, return
a positive indication. Include functions to check if the user input is an actual number,
to see the difference between the inputted number and the randomly generated numbers,
and then compare the numbers.
'''

import random

x = random.randint(0,100)

user_guess = input('Guess the random number - (0-100):')

difference = (user_guess - x)

if user_guess > x:
	print('Your guess is was too high. You were off by:' + str.difference)
elif:
	user_guess < x:
		print('Your guess was too low. You were off by:' + str.difference)
else
	print("You guessed correctly!")