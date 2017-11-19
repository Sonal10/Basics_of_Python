# -*- coding: cp1252 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.

"""
import random as r
num = r.randrange(1,9)

count = 0

while True:
    guess_num = raw_input("Guess the number which computer has selected , its between 1 to 9. OR Enter Exit if you want to end")
    if guess_num == "Exit":
        print "You took {} guesses but couldn't figure out, come back again!".format(count)
        break
    elif int(guess_num) not in range(1,9):
        print "Invalid input, please try again"
        count+=1
    else:
    
        guess_num = int(guess_num)
        if guess_num == num:
            print "Bingo! Exactly right. You guessed it correct."
            print "You took {} guesses".format(count + 1)
            break
        elif guess_num > num:
            print "You guessed too high"
        else:
            print "You guessed too low"
        count +=1
    
