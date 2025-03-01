#1
def multiply(list):
    return eval("*".join(map(str, list)))
    
print(multiply([1,2,4,54,2,3]))

#2 import re

def countLetters(txt):
    capitals = re.findall(r'[A-Z]', txt)
    lowercased = re.findall(r'[a-z]', txt)
    print(f"Upper number: {len(capitals)}; lowercased number: {len(lowercased)}")

countLetters("ABjbJKBDSbfhsjbFDSB")

#3 def isPalindrome(txt):
    return txt == "".join(reversed(txt))
    
print(isPalindrome("pal"))
print(isPalindrome("aba"))

#4
import time
import math

def calculateRoot():
    num = int(input("Num: "))
    milliseconds = int(input("Sleep time: "))
    time.sleep(milliseconds * 0.000001)
    print(f"Square root of num {num} after {milliseconds} milliseconds is: {math.sqrt(num)}")
    return
calculateRoot()  #5 def check(some_tuple):
    return all(some_tuple)
    
arr = ("python", "sql")
print(check(arr))
