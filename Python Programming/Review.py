while True:
    try:
        x = int(raw_input("Please enter an integer:"))
        print "You entered an integer",x
        break

    except ValueError:
        print "Are you fucking kidding me? INTEGER!"

print "You successfully entered an integer!"
