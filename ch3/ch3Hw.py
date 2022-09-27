#Exercise 3.4, 3.6, 3.9, 3.13
#Chapter 2 Exercises
#Carlos Rodriguez Escamilla
#09/13/2022

# 3.4 Geometry: area of a pentagon

# import math

# pentagonSide = eval(input("Enter the pentagon side: "))

# areaOfPentagon= (5 * (pentagonSide ** 2)) / (4 * (math.tan(math.pi/5)))

# print("The area of the pentagon is ", areaOfPentagon)

# 3.6 Fine the character of an ASCII code

# assciiCode = eval(input("Enter an ASCII code: "))
# char = chr(assciiCode)

# print("The character is", char)

# # 3.9 Financial application: payroll

# employeeName = input("Enter employee's name: ")
# hrsWorked = eval(input("Enter number of hours worked in a week: "))
# hrlyPymRate = eval(input("Enter hourly pay rate: "))
# fedTaxRate = eval(input("Enter federal tax withholding rate: "))
# stateTaxRate = eval(input("Enter state tax withholding rate: "))

# grossPay = (hrsWorked * hrlyPymRate)
# fedWithholding = (fedTaxRate * grossPay)
# stateWithholding = (stateTaxRate * grossPay)
# totalDeduction = (fedWithholding + stateWithholding)
# netPay = (grossPay - totalDeduction)

# print("\n")
# print("Employee Name:", employeeName)
# print("Hours Worked:", format(hrsWorked, ".1f"))
# print("Pay Rate:", "${:.2f}".format(hrlyPymRate))
# print("Gross Pay:", "${:.1f}".format(grossPay))
# print("Deductions:")
# print(format("Federal Withholdings (20.0%):", ">31s"),"${:.1f}".format(fedWithholding))
# print(format("State Withholding (9.0%):", ">27s"), "${:.2f}".format(stateWithholding))
# print(format("Total Deduction:", ">18s"), "${:.2f}".format(totalDeduction))
# print("Net Pay: ", "${:.2f}".format(netPay))



# 3.13 Turtle: draw a STOP sign

import turtle

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.left(23)
turtle.begin_fill()
turtle.color("red")
turtle.circle(145, steps=8)
turtle.end_fill()
turtle.goto(0,-100)
turtle.penup()
turtle.goto(-165,-10)
turtle.color("white")
turtle.write("STOP", font=("Verdana", 78, "bold"))
turtle.done()

# See attachment


