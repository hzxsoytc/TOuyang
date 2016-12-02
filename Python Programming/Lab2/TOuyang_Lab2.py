##Author: Tiancheng Ouyang
##Lab: 2
##Date: January 29,2016
##Note: This script is used to define five functions and call each one.

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = float(raw_input("Enter value for x:"))
y = float(raw_input("Enter value for y:"))
z = compare(x,y)
print z
#Question 1, compare x and y


import math
def hypotenuse(x,y):
    z = math.sqrt(x**2 + y**2)
    return z

x = float(raw_input("Enter the length of the first leg:"))
y = float(raw_input("Enter the length of the other leg:"))
z = hypotenuse(x,y)
print "The hypotenuse of the right triangle is", z
#Question 2, calculate hypotenuse

def grade(x):
    if x > 100:
        y = "S"
    elif x >= 97 and x <= 100:
        y = "A+"
    elif x >= 92 and x < 97:
        y = "A"
    elif x >= 88 and x < 92:
        y = "A-"
    elif x >= 85 and x < 88:
        y = "B+"
    elif x >= 81 and x < 85:
        y = "B"
    else:
        y = "0"

    if y == "0":
        return "You did not do very well in this course!"
    elif y == "S":
        return "You are kidding, right?"
    else:
        y = "Your grade is "+y
        return y

x = int(raw_input("Enter your percentaged score of the python course:"))
y = grade(x)
print y
#Question 3, Print grade

def slope(x1,y1,x2,y2):
    k = (y2 - y1)/(x2 - x1)
    return k
def intercept(x1,y1,x2,y2):
    b = y2- (slope(x1,y1,x2,y2) * x2)
    return b
x1 = float(raw_input("Enter the value of x1:"))
y1 = float(raw_input("Enter the value of y1:"))
x2 = float(raw_input("Enter the value of x2:"))
y2 = float(raw_input("Enter the value of y2:"))
print "The equation of the line that goes through the two points you entered is", " y =", slope(x1,y1,x2,y2), "*x + ", intercept(x1,y1,x2,y2)
#Question 4, calculae equation

def inorout(x):
    if x == "USA":
        return 1
    else:
        return 2
def package(x,y):
    if x == 1:
        if y <= 10:
            z = 4 * y
            return z
        elif y <= 20 and y > 10:
            z = 6 * y
            return z
        else:
            z = 0
            return z
    else:
        if y <= 10:
            z = 6 * y
            return z
        elif y <= 20 and y > 10:
            z = 10 * y
            return z
        else:
            z = 0
            return z
        
x = raw_input("Enter the destination of your package, 'USA' or outside:")
y = x.upper()
z = int(raw_input("Enter the weight of your package in kilograms:"))

if z > 20:
    print "Your package is too heavy."
else:
    a = inorout(y)
    b = package(a,z)
    print "The cost of your delivery will be", b
#Question 5, calculate the cost
