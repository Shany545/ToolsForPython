import error as e
def replace():
    blam = input("What file would you like to use(Please include .html/.java/.py/etc)\n")
    blm = input("what would you like to replace?\n")
    bl = input("what would you like to replace it with?\n")

    file = open(blam, "r")
    file2 = file.read()
    file.close()
    file = open(blam, "w")
    if file2.find(blm) != -1:

        file.write(file2.replace(blm, bl))

        print("Action completed!")
    else:
        e.error()
