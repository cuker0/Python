#Exercise 12 (and Solution)
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
#
#Concepts to practice
#Lists and properties of lists
#List comprehensions (maybe)
#Functions

a = [5, 10, 15, 20, 25, 30, 35, 40]
    
def list_ends(a):
    return [a[0], a[-1]]

# Kurde -1 zapamietaj!

print(list_ends(a))