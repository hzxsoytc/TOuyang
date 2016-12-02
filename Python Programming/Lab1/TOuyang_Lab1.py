#Author: Tiancheng Ouyang
#Lab: 1
#Date: January 22,2016
#Note: The five functions are in the order of what PDF mentioned

def birthday(name):
    congratulation= "Happy Birthday" + " " + name + "!"
    print congratulation

birthday("Tiancheng")
#Question 1, Birthday Congratulation

def sum(a,b):
    sum= a + b
    print "The sum of", a, "and", b, "is", sum

sum(2,3)
#Question 2, Sum up two numbers

def power(c,d):
    power= c ** d
    print c, "raised to the power of", d, "is", power

power(3,4)
#Question 3, Power up

import math
def area(r):
    area= (r**2)*math.pi
    print "The the area of a circle with the radius of", r, "is", area

area(5)
#Question 4, Area of the circle

def square(n):
    square=n**2
    print n, "squared gets", square

square(3)
#Question 5, Squared number
