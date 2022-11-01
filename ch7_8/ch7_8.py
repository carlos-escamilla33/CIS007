# Exercises 7.3, 7.5, 8.4
# Chapters 7 and 8 Exercises
# Carlos Rodriguez Escamilla
# 10/31/2022

# 7.3 The Account class

# UML Diagram
"""
    Account

    -id: int
    -balance: float
    -annualInterestRate: float

    Account(id: int, balance: float, annualInterestRate: float)
    getId(): int
    getBalance(): float
    getAnnualInterest(): float
    setId(id: int): None
    setBalance(balance: float): None
    setAnnualInterestRate(annualInterestRate: float): None
    getMonthlyInterestRate(): float
    getMonthlyInterest(): float
    withdraw(amount: float): None
    deposit(amount: float): None

"""

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
        if id >= 0:
            self.__id = id
        else:
            print(f"Enter an id greater than {id}")
    
    def setBalance(self, balance = 0.0):
        if balance > 0.0:
            self.__balance = balance
        else:
            print(f"Enter a balance greater than {balance}")

    def setAnnualInterestRate(self, annualInterestRate = 0.0):
        if annualInterestRate > 0.0:
            self.__annualInterestRate = annualInterestRate
        else:
            print(f"Enter an annual interest rate greater than {annualInterestRate}")

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12
    
    def getMonthlyInterest(self):
        return round(self.__balance * self.getMonthlyInterestRate(), 2)
    
    def withdraw(self, amount = 0):
        self.__balance = self.__balance - amount
    
    def deposit(self, amoount = 0):
        self.__balance = self.__balance + amoount

account1 = Account(1122, 20000, 4.5)
account1.withdraw(2500)
account1.deposit(3000)

accId = account1.getId()
accBalance = account1.getBalance()
accMonthlyInterestRate = account1.getMonthlyInterestRate()
accMonthlyInterest = account1.getMonthlyInterest()

# print(f"The id is {accId}")
# print(f"The balance of the account is ${'{:,}'.format(accBalance)}")
# print(f"The monthly interst of the account is {accMonthlyInterestRate}%")
# print(f"The annual interest of the account is ${accMonthlyInterest}")

# 7.5 Geometry: n sided regular polygon

# UML Diagram
"""
    RegularPolygon

    -n: int
    -side: float
    -x: float
    -y: float

    RegularPolygon(n: int, side: float, x: float, y: float)
    getN(): int
    getSide(): float
    getX(): float
    getY(): float
    setN(n: int): None
    setSide(side: float): None
    setX(x: float): None
    setY(y: float): None
    getPerimeter(): float
    getArea(): float

"""

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
    
    def setN(self, n = 0):
        if n > 2:
         self.__n = n
        else:
            print(f"Enter an n greater than {n}")
    
    def setSide(self, side = 1.0):
        if side > 0.0:
            self.__side = side
        else:
            print(f"Enter a side greater than {side}")
    
    def setX(self, x = 0.0):
        if x >= 0.0:
            self.__x = x
        else:
            print(f"Enter a value for x greater than {x}")
    
    def setY(self, y = 0.0):
        if y >= 0.0:
            self.__y = y
        else:
            print(f"Enter a value for x greater than {y}")

    def getPerimeter(self):
        perimeter = self.__n * self.__side
        return perimeter

    def getArea(self):
        import math
        area = (self.__n * (math.pow(self.__side, 2))) / (4 * math.tan(math.pi / self.__n))
        return area
    

poly1 = RegularPolygon()
poly2 = RegularPolygon(6, 4)
poly3 = RegularPolygon(10, 4, 5.6, 7.8)

# print(f"Polygon1 has a perimeter of {poly1.getPerimeter()} and area is {format(poly1.getArea(), '.2f')}")
# print(f"Polygon2 has a perimeter of {poly2.getPerimeter()} and area is {format(poly2.getArea(), '.2f')}")
# print(f"Polygon3 has a perimeter of {poly3.getPerimeter()} and area is {format(poly3.getArea(), '.2f')}")

# 8.4 Occurrences of a specified character

def count(s, targetCh):
    charCount = 0

    for char in s:
        if char.__eq__(targetCh):
            charCount+=1

    return charCount

def main():
    userInput = input("Enter any word:")
    charToCount = input("Which character would you like to count the occurences of?:")

    chrCountResult = count(userInput, charToCount)

    if chrCountResult.__eq__(1):
        print(f"The character '{charToCount}' shows up {chrCountResult} time in {userInput}")
    else:
         print(f"The character '{charToCount}' shows up {chrCountResult} times in {userInput}")

main()