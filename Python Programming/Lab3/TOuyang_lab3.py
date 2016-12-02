##Aruthor: Tiancheng Ouyang
##Lab: 3
##Date: February 5,2016
##Note: This script is used to define six functions and then call each one

def isBetween(x,y,z):
    if y <= x <= z:
        return "True"
    else:
        return "False"
x = float(raw_input("Enter value for x:"))
y = float(raw_input("Enter value for y:"))
z = float(raw_input("Enter value for z:"))
print isBetween(x,y,z)
##Question 1

def printBack(text):
    length = len(text)
    n = length
    while 1 <= n <= length:
        last_letter = text[n-1]
        print last_letter
        n = n -1
text = raw_input("Enter the string:")
printBack(text)
##Question 2

prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter == "O":
        print "Ou" + suffix
    elif letter == "Q":
        print "Qu" + suffix
    else:
        print letter + suffix
##Question 3

def countLetters(text,check):
    count = 0
    for letter in text:
        if letter == check:
            count = count + 1
    if count == 0:
        count = -1
    return count
text = raw_input("Enter the string you wish to check:")
check = raw_input("Enter the letter you wish to count in the string:")
print countLetters(text,check)
##Question 4

a = int(raw_input("Enter the first number between 1 and 30:"))
b = int(raw_input("Enter the second number between 1 and 30:"))
c = int(raw_input("Enter the third number between 1 and 30:"))
d = int(raw_input("Enter the fourth number between 1 and 30:"))
e = int(raw_input("Enter the fifth number between 1 and 30:"))
numbers = [a,b,c,d,e]
for number in numbers:
    if number < 1 or number > 30:
        print "Please follow the insturctions"
    else:
        print number * "*"
##Question 5

def isPrime(n):  
    if n <= 1:  
        return False 
    i = 2 
    while i*i <= n:  
        if n % i == 0:  
            return False 
        i += 1 
    return True
numberList = range(1,101)
for number in numberList:
    if isPrime(number) == True:
        print number
##Question 6

def printStars():
    n = 0
    while n <= 5:
        print " " * (5 - n) + "*" * (2*n - 1)
        n += 1
    while 5 < n <= 9:
        print " " * (n - 5) + "*" * (19 - 2*n)
        n += 1
printStars()
##Bonus
