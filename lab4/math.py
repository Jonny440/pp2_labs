#1
import math

degree = float(input("Input degree"))
print(degree * math.pi / 180)


#2
import math

height = float(input("Height: "))
baseOne = float(input("Base1: "))
baseTwo = float(input("Base2: "))
print(height * (baseOne + baseTwo) / 2)


#3
import math
sideNumber = int(input("Number of sides: "))
length = float(input("Length: "))

apothem = length / (2 * math.tan(math.pi / sideNumber))
area = (length * sideNumber * apothem) / 2

print(area)


#4
import math

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

print(base * height)