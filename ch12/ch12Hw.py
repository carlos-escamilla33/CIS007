# Exercise 12.1
# Chapter 12
# Carlos Rodriguez Escamilla
# 11/12/2022

# 12.1 The Triangle Class

"""
    GeometricObject
    -color: str
    -filled: bool

    GeometricObject(color: str, filled: bool)
    getColor(): str
    setColor(color: str): None
    isFilled(): bool
    setFilled(filled: bool): None
    __str__(): str
"""

import math


class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return bool(self.__filled)

    def setFilled(self, filled):
        if filled == 0 or filled == 1:
            self.__filled = filled
        else:
            print("Oops, enter 1 for filled, or 0 for a blank triangle.")
    
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)


"""
    Triangle
    -side1: float
    -side2: float
    -side3: float

    Triangle(color: str, filled: int, side1: float, side2: float, side3: float)
    getSide1(): float
    getSide2(): float
    getSide3(): float
    setSide1(side1: float): None
    setSide2(side2: float): None
    setSide3(side3: float): None
    getArea(): float
    getPerimeter(): float
    __str__(): str
"""

class Triangle(GeometricObject):
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3
    
    def setSide1(self, side1):
        if side1 > 0:
            self.__side1 = side1
        else:
            print("Enter a side1 greater than zero.")
    
    def setSide2(self, side2):
        if side2 > 0:
            self.__side2 = side2
        else:
            print("Enter a side2 greater than zero")
    
    def setSide3(self, side3):
        if side3 > 0:
            self.__side3 = side3
        else:
            print("Enter a side3 greater than zero")

    def getArea(self):
        semiPerimeter = ((self.__side1 + self.__side2 + self.__side3) / 2)
        area = round(math.sqrt((semiPerimeter * (semiPerimeter - self.__side1) * (semiPerimeter - self.__side2) * (semiPerimeter - self.__side3))), 3)
        return area
    
    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + \
            str(self.__side2) + " side3 = " + str(self.__side3)
        

def main():
    side1, side2, side3 = eval(input("Enter three triangle sides (comma separated): "))
    triangleColor = input("Enter triangle color: ")
    isTriangleFilled = eval(input("Enter 1 to fill triangle with color. 0 for unfilled: "))

    triangle = Triangle(triangleColor, isTriangleFilled, side1, side2, side3)

    area = triangle.getArea()
    perimeter = triangle.getPerimeter()
    color = triangle.getColor()
    isFilled = triangle.isFilled()

    print(f"\n{triangle}")
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
    print(f"Color: {color}")
    print(f"Is Filled: {isFilled}")


main()
    


 
