letterCounts = {}
for letter in "Mississippi":
    letterCounts[letter] =  letter.get (letter, 0) + 1

print letterCounts
letterItems = letterCounts.items()
letterItems.sort()
print letterItems
