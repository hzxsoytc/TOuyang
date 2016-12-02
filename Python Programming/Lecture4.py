##count1 = 0
##count2 = 0
##for number in range(1,101):
##    if number % 2 ==0:
##        count1 += 1
##    else:
##        count2 += 1
##print "There are", count1, "odd numbers"
##print "There are", count2, "even numbers"
##
##evenSum = 0
##oddSum = 0
##
##for number in range(1,101):
##    if number % 2 == 0:
##        evenSum += number
##    else:
##        oddSum += number
##print evenSum
##print oddSum
##
##nestedList = ['spam!','1',['Brie','Roquefort','Dol'],[1,2,3]]
##print len(nestedList)
##for n in nestedList:
##    print n
##
##def head(list):
##    return list[0]
##numbers = [1,2,3]
##print head(numbers)
##
##def min_max(t):
##	return min(t), max(t)
##list_t = range(1,10)
##min, max = min_max(list_t)
##print min, max

import string
list = ['c','l','a','s','s']
print string.join(list,'')
