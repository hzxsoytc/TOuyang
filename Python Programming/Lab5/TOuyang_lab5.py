##Aruthor: Tiancheng Ouyang
##Lab: 4
##Date: February 12,2016
##Note: This script is used to define six functions and then call each one

def Q1(myfile):
    myfile = open(myfile,"r")
    identifier = []
    borough = []
    school_name = []
    school_enrollment = []
    x_coordinate = []
    y_coordinate = []
    for line in myfile:
        lineElement = line.split('\t')
        identifier.append(lineElement[0])
        borough.append(lineElement[1])
        school_name.append(lineElement[2])
        school_enrollment.append(lineElement[3])
        x_coordinate.append(lineElement[4])
        y_coordinate.append(lineElement[5])
    myfile.close()    ##separate each kind of information into different lists

    def averageEnrollment(a,b):
        i = 0
        sum_a = 0.00
        count = 0
        while i < len(identifier):
            if a[i] == b:
                sum_a += int(school_enrollment[i])
                count += 1
            i += 1
        average = sum_a / count
        return b,average    ##Calculate average for every category
    Q1 = {}
    Q1['MN'] = averageEnrollment(borough,'MN')[1]
    Q1['BX'] = averageEnrollment(borough,'BX')[1]
    Q1['BK'] = averageEnrollment(borough,'BK')[1]
    Q1['QN'] = averageEnrollment(borough,'QN')[1]
    Q1['SI'] = averageEnrollment(borough,'SI')[1]       ##Manually input all the information needed into the list
    Question1 = open('Question1.txt',"w")
    first = Q1.keys()
    second = Q1.values()
    i = 0
    while i < len(first):
        seq = [str(first[i]),'\t','%5.2f'%(second[i]),'\n']      ##Define a sequence to be input as evey line
        Question1.writelines(seq)       ##Write every sequence as a line
        i += 1
    Question1.close()

Q1('nycSchools.txt')

def Q2(myfile):
    myfile = open(myfile,"r")
    identifier = []
    borough = []
    school_name = []
    school_enrollment = []
    x_coordinate = []
    y_coordinate = []
    for line in myfile:
        lineElement = line.split('\t')
        identifier.append(lineElement[0])
        borough.append(lineElement[1])
        school_name.append(lineElement[2])
        school_enrollment.append(lineElement[3])
        x_coordinate.append(lineElement[4])
        y_coordinate.append(lineElement[5])
    myfile.close()    ##separate each kind of information into different lists

    def proportion(a):
        i = 0
        count = 0
        while i < len(identifier):
            if borough[i] == a:
                count += 1
            i += 1
        prop = float(count) / len(identifier)
        return prop
    print "The proportion of the schools located in Manhattan is", '%4.2f'%(proportion('MN')*100),"%"

Q2('nycSchools.txt')

def Q3(myfile):
    myfile = open(myfile,"r")
    identifier = []
    borough = []
    school_name = []
    school_enrollment = []
    x_coordinate = []
    y_coordinate = []
    for line in myfile:
        lineElement = line.split('\t')
        identifier.append(lineElement[0])
        borough.append(lineElement[1])
        school_name.append(lineElement[2])
        school_enrollment.append(lineElement[3])
        x_coordinate.append(lineElement[4])
        y_coordinate.append(lineElement[5])
    myfile.close()    ##separate each kind of information into different lists

    def over700(a,b):
        i = 0
        count = 0
        while i < len(identifier):
            if a[i] == b and school_enrollment[i] > 700:
                count += 1
            i += 1  ##calculate qualified school number using loop
        return b,count
    Q3 = {}
    Q3['MN'] = over700(borough,'MN')[1]
    Q3['BX'] = over700(borough,'BX')[1]
    Q3['BK'] = over700(borough,'BK')[1]
    Q3['QN'] = over700(borough,'QN')[1]
    Q3['SI'] = over700(borough,'SI')[1]
    Question3 = open('Question3.txt',"w")
    first = Q3.keys()
    second = Q3.values()
    i = 0
    while i < len(first):
        seq = [str(first[i]),'\t',str((second[i])),'\n']      ##Define a sequence to be input as evey line
        Question3.writelines(seq)       ##Write every sequence as a line
        i += 1
    Question3.close()

Q3('nycSchools.txt')

def Q4(myfile):
    myfile = open(myfile,"r")
    identifier = []
    borough = []
    school_name = []
    school_enrollment = []
    x_coordinate = []
    y_coordinate = []
    for line in myfile:
        lineElement = line.split('\t')
        identifier.append(lineElement[0])
        borough.append(lineElement[1])
        school_name.append(lineElement[2])
        school_enrollment.append(lineElement[3])
        x_coordinate.append(lineElement[4])
        y_coordinate.append(lineElement[5])
    myfile.close()    ##separate each kind of information into different lists

    def minmax(a):
        maxcoordinate = a[0]
        mincoordinate = a[0]
        for num in a:
            if num > maxcoordinate:
                maxcoordinate = num  ##Find maximum through loop
            if num < mincoordinate:
                mincoordinate = num  ##Find miminum through loop
        return mincoordinate, maxcoordinate

    print "Mininum x=:",minmax(x_coordinate)[0],'\t',"Maximum x=:",minmax(x_coordinate)[1]
    print "Mininum y=:",minmax(y_coordinate)[0],'\t',"Maximum y=:",minmax(y_coordinate)[1]

Q4('nycSchools.txt')

def Q5(myfile):
    myfile = open(myfile,"r")
    letterCounts = {}
    alist = []
    blist = []
    for line in myfile:
        lineElement = line.split(' ')   ##Separate every word in the sentence
        for letter in lineElement:
            alist.append(letter)       ##Input all the separated word into a list
    for ele in alist:
        letterCounts[ele[0]]=letterCounts.get(ele[0],0) + 1 ##Count all the words in the list that start with the same letter
    for key in letterCounts:
        blist.append(key*letterCounts[key]) ##Duplicate the letter by the times it appears
        blist.sort()
    for ele in blist:
        print ele   ##Print the duplicated list
    myfile.close()

Q5('question_5.txt')

def Q6(myfile):
    import math
    myfile = open(myfile,"r")
    identifier = []
    x_coordinate = []
    y_coordinate = []
    mindistance = []
    sumDist = 0
    for line in myfile:
        lineElement = line.split('\t')
        identifier.append(lineElement[0])
        x_coordinate.append(lineElement[4])
        y_coordinate.append(lineElement[5])
    myfile.close()
    i = 0
    while i < len(identifier) - 1:
        mindist = 1000000
        j = 0
        while j < len(identifier) and j != i:
            dist = math.hypot (float(x_coordinate[j]) - float(x_coordinate[i]), float(y_coordinate[j]) - float(y_coordinate[i])) ##Calculate distance between each point and the following point
            if dist < mindist:
                mindist = dist  ##Calculate minimum distance
            j += 1  ##For every point, loop through the rest points
        mindistance.append(mindist)
        i += 1
    for figure in mindistance:
        sumDist += figure
    print sumDist / len(mindistance)
Q6(r'D:\Tiancheng Ouyang\Python Programming\Lab5\nycSchools.txt')
