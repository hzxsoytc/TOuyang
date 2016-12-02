def absolute(x):
    if x < 0:
        y = -x
    else:
        y = x
    return y

x = int(raw_input("Enter an integer:"))
z = absolute(x)
print z
