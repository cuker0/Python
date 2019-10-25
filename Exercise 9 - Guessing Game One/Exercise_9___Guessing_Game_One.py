#Exercise 9 (and Solution)
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
#Extras:
#
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
number = random.randint(1,9)
print(number)
count = 0
guess = 0

while guess != number and guess !="exit":
    guess = int(input("Choose value from 1 to 9: "))
    count +=1
    if guess == "exit":
     break

    if number>guess:
     print("Value too low")
    elif number<guess:
     print("Value too high")
    else:
       print("Lucky shot. It took you",count,"tries!")
