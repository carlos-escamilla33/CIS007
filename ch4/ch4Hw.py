#Exercise 4.7, 4.11, 4.12, 4.17
#Chapter 4 Exercises
#Carlos Rodriguez Escamilla
#09/25/2022

# 4.7 ComputeChange

# Recieve the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickles = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

print("Your amount ", amount," consists of")

if numberOfDollars != 1:
    print(numberOfDollars," dollars")
else:
    print(print(numberOfDollars," dollar"))

if numberOfQuarters != 1:
    print(numberOfQuarters," quarters")
else:
    print(numberOfQuarters," quarter")

if numberOfDimes != 1:
    print(numberOfDimes," dimes")
else:
    print(numberOfDimes," dime")

if numberOfNickles != 1:
    print(numberOfNickles," nickles")
else:
    print(numberOfNickles," nickle")

if numberOfPennies != 1:
    print(numberOfPennies," pennies")
else:
    print(numberOfPennies,"penny")


# 4.11 Find the number of days in a month

month = input("Enter month: ").lower()
year = eval(input("Enter year: "))
isLeap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

if month == "february" and isLeap:
    print(month.title(), year, "has 29 days")
elif month == "february":
    print(month.title(), year, "has 28 days")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print(month.title(), year, "has 30 days")
else:
    print(month.title(), year, "has 31 days")


# 4.12 Check a number

numInput = eval(input("Enter an integer: "))

if numInput % 5 == 0 and numInput % 6 == 0:
    print("Is", numInput, "divisible by 5 and 6? True")
else:
    print("Is", numInput, "divisible by 5 and 6? False")

if numInput % 5 == 0 or numInput % 6 == 0:
    print("Is", numInput, "divisible by 5 or 6? True")
else:
    print("Is", numInput, "divisible by 5 or 6? False")

if (numInput % 5 == 0 and numInput % 6 != 0) or (numInput % 5 != 0 and numInput % 6 == 0):
    print("Is", numInput, "divisible by 5 or 6, but not both? True")
else:
    print("Is", numInput, "divisible by 5 or 6, but not both? False")


# 4.17 Game: scissor, rock, paper

import random

playerMove = eval(input("Scissor(0), rock(1), paper(2): "))
playerWeapon = ""
computerMove = random.randint(0,2)
computerWeapon = ""
playerWin = True
tieGame = False

if playerMove == 0:
    playerWeapon = "Scissor"
if computerMove == 0:
    computerWeapon = "Scissor"
if playerMove == 1:
    playerWeapon = "Rock"
if computerMove == 1:
    computerWeapon = "Rock"
if playerMove == 2:
    playerWeapon = "Paper"
if computerMove == 2:
    computerWeapon = "Paper"

if playerMove == computerMove:
    tieGame = True
elif playerMove == 0 and computerMove == 1:
    playerWin = False
elif playerMove == 1 and computerMove == 2:
    playerWin = False
elif playerMove == 2 and computerMove == 0:
    playerWin = False

if tieGame:
    print(f"The computer is {computerWeapon}. You are {playerWeapon} too. It is a draw!")
elif playerWin:
    print(f"The computer is {computerWeapon}. You are {playerWeapon}. You Win!")
else:
    print(f"The computer is {computerWeapon}. You are {playerWeapon}. You lose!")




