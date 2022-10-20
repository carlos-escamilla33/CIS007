# # RandChars.py

import random
    
def main():
    # print("Random numbers between 97 and 122 are:")
    evenNumsCount = 0

    for _ in range(15):
        randomNum = random.randint(97, 122)
        print(randomNum, end=" ")
        if randomNum % 2 == 0:
            evenNumsCount+=1
    
    print("\nCount of even numbers is:", evenNumsCount)

    print("Random lower case letters are:")
    nonVowelCount = 0

    while True:
        randomNum = random.randint(97, 122)

        print(chr(randomNum), end=" ")
        nonVowelCount+=1

        if randomNum == 97:
            break
        elif randomNum == 101:
            break
        elif randomNum == 105:
            break 
        elif randomNum == 111:
            break 
        elif randomNum == 117:
            break

    if nonVowelCount != 1:
        print(f"\nIt took {nonVowelCount} tries to get a vowel")
    else:
        print(f"\nIt took {nonVowelCount} try to get a vowel")


main()

# insurance 

# import math


# def premium(customerAge):
#     customerPremium = ((math.floor(customerAge / 10)) + 15) * 21.3
#     return customerPremium

# def main():
#     print(f"{'Age':<6}Insurance Premium")
#     for age in range(18, 79, 10):
#         getPremium = premium(age)

#         print(f"{age :>3} {'$':>7} {format(getPremium, '0.1f')}")

# main()
