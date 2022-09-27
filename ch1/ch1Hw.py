#Exercise 1.4, 1.9, 1.15, (1.11), (1.18)
#Chapter 1 Exercises
#Carlos Rodriguez Escamilla
#09/01/2022

# 1.4
# (Print a table) Write a program that displays a table

print('''
    a   a^2  a^3
    1   1    1
    2   4    8
    3   9    27
    4   16   64
''')


# 1.9 Area and perimeter of a rectangle

print("The area of the rectangle is", 4.5 * 7.9)
print("The perimeter of the rectangle is", 2 * (4.5 + 7.9))

# 1.15 Write a program that draws two triangles as shown in figure 1.18d

import turtle

turtle.showturtle()
turtle.goto(50, 100)
turtle.left(180)
turtle.forward(100)
turtle.goto(0,0)
turtle.goto(50, -100)
turtle.forward(100)
turtle.goto(0,0)
turtle.done()