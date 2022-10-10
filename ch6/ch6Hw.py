# Exercises 6.9, 6.11, 6.12, 6.18

# 6.9 Covert from feet to meters

def feetToMeters(feet):
    meters = 0.305 * feet
    return meters

def metersToFeet(meters):
    feet = meters / 0.305
    return feet

def tableHeader():
    print(f"{'Feet' :<8}{'Meters' :<7} | {'Meters' :<8}{'Feet' :<7}")
    print()

def displayTable():
    for i in range(1, 11):
        print(f"{format(i, '0.1f') :<8}{format(feetToMeters(i), '0.3f') :<7} | " + 
        f"{format(15+i * 5, '0.1f') :<8}{format(metersToFeet(15+i * 5), '0.3f') :<7}")

# tableHeader()
# displayTable()

# 6.11 

# base salary = 5000
# base salary + commission

# 6.12 Display characters

def printChars(ch1, ch2, numberPerLine):
    start = ord(str(ch1))
    end = ord(str(ch2))
    charCount = 0

    for i in range(start, end + 1):
        charCount+=1
        if charCount % numberPerLine == 0:
            print(chr(i), end="\n")
        else:
            print(chr(i), end=" ")

# printChars(1, 'Z', 10)

# 6.18 Display matrix of 0s and 1s
import random

def printMatrix(n):
    digitCount = 0

    for _ in range(n * n):
        randomDigit = random.randint(0,1)
        digitCount+=1

        if digitCount % n == 0:
            print(randomDigit, end="\n")
        else:
            print(randomDigit, end=" ")

# printMatrix(3)









