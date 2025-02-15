#Generetors
#1
def squareGen(limit):
    counter = 1
    double = 1
    while counter <= limit:
        yield double
        counter += 1
        double = counter ** 2

N = int(input("Input: "))
gen = squareGen(N)
for square in gen:
    print(square)
    

#2
def evens(lim):
    for i in range(0, lim):
        if i % 2 == 0:
            yield i

N = int(input("Input: "))
generator = evens(N)
for even in generator:
    print(even)


#3
def divisible(lim):
    for i in range(0, lim + 1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

N = int(input("Input: "))
generator = divisible(N)
for even in generator:
    print(even)


#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Start: "))
b = int(input("End: "))

generator = squares(a, b)
for square in generator:
    print(square)


#5
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Start: "))
b = int(input("End: "))

generator = squares(a, b)
for square in generator:
    print(square)
