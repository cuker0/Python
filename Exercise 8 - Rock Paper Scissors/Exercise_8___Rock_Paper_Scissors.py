#Exercise 8 (and Solution)
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
#
#Remember the rules:
#
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

import sys

answer = "Y"

while (answer != "N"):
    player1 = input("Choose from P-paper,S-scissors,R-rock: ")
    player2 = input("Choose from P-paper,S-scissors,R-rock: ")
    if (player1 =="P" and player2 =="R") or (player2 =="P" and player1 =="R"):
        print("Paper Wins!")
    elif (player1 =="S" and player2 =="P") or (player2 =="S" and player1 =="P") :
        print("Scissors Wins!")
    elif (player1 =="R" and player2 =="S") or (player2 =="R" and player1 =="S") :
        print("Rock Wins!")
    else:
     print("Invalid input! You have not entered rock, paper or scissors, try again.")
    answer = input("Try again?: Y,N: ")


