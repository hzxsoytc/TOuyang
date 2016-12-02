##letterCounts = {}
##for letter in "Mississippi":
##	letterCounts[letter] = letterCounts.get (letter,0) + 1
##print letterCounts
##
##def getString(damn):
##    string = {}
##    for item in damn:
##        string[item] = string.get(item,0) + 1
##    stringItems = string.items()
##    return stringItems
##print getString(raw_input("Enter a string:"))
##
##f = open("test.dat","w")
##print f
##type(f)
##f.write("Holy crap\n")
##f.write("Holy shit\n")
##f.close()
##f = open("test.dat","r")
##text = f.read()
##print text

def filterFile(oldFile,newFile):
    f1 = open(oldFile,"r")
    f2 = open(newFile,"w")
    while True:
        text = f1.readline()
        if text == "":
            break
        if text[0] == '#':
            continue
        f2.write(text)
    f1.close()
    f2.close()
    return

filterFile(r"D:\Tiancheng Ouyang\Python Programming\test.dat",r"D:\Tiancheng Ouyang\Python Programming\empty.dat")
