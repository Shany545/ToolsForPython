import os.path
def python():
    namethefile = input("INPUT THE NAME OF THE FILE \n")

    if os.path.isfile(namethefile+".py"):
        files = open(namethefile+".py","r+")
    else:
        files = open(namethefile+".py","x")
        files.close()
        files = open(namethefile+".py","r+")

    files.write("import random \n import time \n ")

    files.close()

    print("File created!")
python()
