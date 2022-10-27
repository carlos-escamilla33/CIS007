# Exercises 7.3, 7.5, 8.4
# Chapters 7 and 8 Exercises
# Carlos Rodriguez Escamilla
# 10/26/2022

# 7.3 How do you create an object?

class Account:
    def __init__ (self, id = 0, balance = 100.0, annualInterestRate = 10.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def setId(self, id = 0):
        self.__id = id
    
    def setBalance(self, balance = 0):
        self.__balance = balance
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    
    def credit(self, amount = 0):
        self.__balance = self.__balance + amount
    
    def debit(self, amount = 0):
        self.__balance = self.__balance - amount
    
    def getMonthlyInterest(self):
        return self.__balance * (self.__annualInterestRate / 12)
