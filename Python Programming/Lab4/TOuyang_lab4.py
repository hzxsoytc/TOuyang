##Aruthor: Tiancheng Ouyang
##Lab: 4
##Date: February 12,2016
##Note: This script is used to define six functions and then call each one

def squareList():
    list1 = range(1,11)
    i = 0
    while i < len(list1):
        list1[i] = list1[i] ** 2
        i += 1
    return list1
print squareList()
#Question 1

def countList():
    numList = [21,25,32,92,42,58,65,83,18]
    countNum = 0
    sumNum = 0
    checkNum = 37
    for num in numList:
        if num > checkNum:
            sumNum += num
            countNum += 1
    average = sumNum / countNum
    return countNum, average    
a = countList() ##Return a tuple
print "There are", a[0], "numbers in the list that is larger than 37"
print "Their average is", a[1]
#Question 2

def minmax():
    grades = [92,78,99,83,76,89,60,84]
    maxgrade = 0
    mingrade = 2000
    for num in grades:
        if num > maxgrade:
            maxgrade = num
            ##Find maximum through loop
        if num < mingrade:
            mingrade = num
            ##Find miminum through loop
    return maxgrade, mingrade
a = minmax()
print "The minimum grade is", a[1]
print "The maximum grade is", a[0]
## Question 3

def lineMatrix():
    lineList = []
    i = 0
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            lineList.append(matrix[i][j])
            j += 1 ##Loop in every element
        i += 1  ##Loop in every line
    return lineList
b = lineMatrix() 
print "The new list is", b
## Question 4

oldList = ['grade','wide','den','day']
newList = []
a = 'd'
b = 'p'
def replace(oldList,a,b):
    i = 0
    for num in oldList:
        newWord = ''
        for letter in oldList[i]:
            if letter == a:
                newWord = newWord + b
            else:
                newWord = newWord + letter
        i += 1
        newList.append(newWord)
    return newList
c = replace(oldList,a,b)
print "The transformed words are", c
