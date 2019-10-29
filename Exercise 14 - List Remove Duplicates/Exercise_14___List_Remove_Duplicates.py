#Exercise 14 (and Solution)
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
#Extras:
#
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.
#Discussion
#Concepts for this week:
#
#Sets

import random

a = []
b = []
c = []

digit = int(input("Value:"))

def comparing(digit):
    for i in range(digit):
     a.append(random.randint(0,9))
     b.append(random.randint(0,9))
pass    

# wartosc range do podania zakresu petli FOR!!
comparing(digit)
c = set(a+b)

print(a)
print(b)
print(list(c))