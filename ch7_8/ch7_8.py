# Exercises 7.3, 7.5, 8.4
# Chapters 7 and 8 Exercises
# Carlos Rodriguez Escamilla
# 10/26/2022

# 7.3 The Account class

# UML Diagram



class Account:
    def __init__ (self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterest(self):
        return self.__annualInterestRate
    
    def setId(self, id = 0):
        self.__id = id
    
    def setBalance(self, balance = 0.0):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return round(self.__annualInterestRate / 12, 2) / 100
    
    def getMonthlyInterest(self):
        return self.__balance * (self.getMonthlyInterestRate())
    
    def withdraw(self, amount = 0):
        self.balance = self.__balance - amount
    
    def deposit(self, amoount = 0):
        self.balance = self.balance + amoount

account1 = Account(1122, 20000, 4.5)

# account1.withdraw(2500)
# account1.deposit(3000)

# print(account1.getId())
# print(account1.getBalance())
# print(account1.getAnnualInterest())
# print(account1.getMonthlyInterest())

# 7.5 Geometry: n sided regular polygon

class RegularPolygon:
    def __init__(self, n = 3, side = 1.0, x = 0.0, y = 0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def getN(self):
        return self.__n
    
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setN(self, n):
        self.__n = n
    
    def setSide(self, sides):
        self.__side = sides
    
    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        perimeter = self.getN() * self.getSide()
        return perimeter

    def getArea(self):
        apothem = self.getSide()
        area = (self.getN * self.getSide())
    

