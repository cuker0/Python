#Exercise 4 (and Solution)
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

digit = int(input("Number to check all divisors:"))
divisors= []
#Nalezy stworzyc liste odpytan urzadzenia
listRange = list(range(1,digit+1))

for i in listRange:
 
 if digit % i == 0:
  divisors.append(i)
 
print(divisors)