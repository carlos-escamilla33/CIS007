#Exercise 2.5, 2.13, 2.15, 2.19
#Chapter 2 Exercises
#Carlos Rodriguez Escamilla
#09/11/2022

# 2.5 Financial Application: calculate tips

subtotal, gratuityRate = eval(input("Enter subtotal and a gratuity rate: "))

gratuity = subtotal * (gratuityRate / 100)
total = subtotal + gratuity

print("The gratuity is ", round(gratuity,2) , " and the total is ", round(total,2))

# 2.13 Split Digits

num1, num2, num3, num4= input("Enter a four digit integer: ")

print(num1)
print(num2)
print(num3)
print(num4)


# 2.15 Geometry: Area of a hexagon

hexSide = eval(input("Enter side of hexagon: "))
hexArea = ((3 * (3 ** 0.5)) / 2) * (hexSide ** 2)

print(round(hexArea, 4))

# 2.19 Financial application: calculate future investment value

investmentAmt = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
numOfYears = eval(input("Enter number of years: "))

monthlyInterestRate = ((annualInterestRate / 100) / 12)
numOfMonths = (numOfYears * 12)

futureInvestmentVal = (investmentAmt * (1 + monthlyInterestRate) ** numOfMonths)

print("Accumulated value is ",round(futureInvestmentVal, 2))
