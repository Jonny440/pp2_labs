#1
class Student:
    def __init__(self):
       name = "None"
      
    def getName(self):
        self.name = input("Enter your nmaame")
    
    def printName(self):
        print(self.name.upper())
    
me = Student()
me.getName()
me.printName()

#2-3
class Shape:
    def __init__(self):
        self.area = 0
    
    def printArea(self):
        print(self.area)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def findArea(self):
        self.area = self.length * self.width
        
book = Rectangle(5, 6)
book.findArea()
book.printArea()

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x)
        print(self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, point):
        distance = math.sqrt((self.y - point.y) * (self.y - point.y) + (self.x - point.x) * (self.x - point.x))
        print(distance)

pointOne = Point(2, 3)
pointTwo = Point(-1, 5)
pointOne.show()
pointOne.move(2, 2)
pointOne.dist(pointTwo)

#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
    def showBalance(self):
        print(self.balance)
        
business = Account("Jong Chi", 500)
business.deposit(4000)
business.withdraw(10000)
business.showBalance()

#6
def isPrime(num):
    if num == 1 or num == 2:
        return True
    
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True
    
arr = [1,2,7,12,15,17,21]
onlyPrimes = list(filter(lambda num: isPrime(num), arr))
nonPrimes = list(filter(lambda num: not isPrime(num), arr))

print(onlyPrimes)
print(nonPrimes)
