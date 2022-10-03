# Exercises 5.3, 5.15, 5.17, 5.29

# 5.3 Conversion from kilograms to pounds
print(f"{'Kilograms':<13}{'Pounds':<10}")
print()
conversionNum = 2.2

for i in range(1,200):
    print(f"{i :< 13}{round(i * conversionNum, 1) :<10}")

# 5.15 Find the largest n such that n^3 < 12,000
largestNum = -1
i = 0
while pow(i, 3) < 12000:
    if i > largestNum:
        largestNum = i
    i+=1

print(largestNum)

