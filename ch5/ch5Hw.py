# Exercises 5.3, 5.15, 5.17, 5.29

# 5.3 Conversion from kilograms to pounds
# print(f"{'Kilograms':<13}{'Pounds':<10}")
# print()
# conversionNum = 2.2

# for i in range(1,200):
#     print(f"{i :< 13}{round(i * conversionNum, 1) :<10}")

# 5.15 Find the largest n such that n^3 < 12,000
# largestNum = -1
# i = 0
# while pow(i, 3) < 12000:
#     if i > largestNum:
#         largestNum = i
#     i+=1

# print(largestNum)

# 5.17 Display ASCII character table

# start = ord("!")
# end = ord("~") + 1
# count = 0
# for i in range(start, end):
#     count+=1
#     if count % 10 == 0:
#         print(chr(i), end="\n")
#     else:
#         print(chr(i), end=" ")

# 5.29 Display Leap Years

yrCurrent = 2001
yrEnd = 2100
count = 0

while yrCurrent <= yrEnd:
    count+=1 
    if yrCurrent % 4 == 0 and not(yrCurrent % 100 == 0):
        if count % 10 == 0:
            print(yrCurrent, end="\n")
        else:
            print(yrCurrent, end=" ")   
    yrCurrent+=1