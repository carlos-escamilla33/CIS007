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

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
    
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)

 
