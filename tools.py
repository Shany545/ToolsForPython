import os.path
import sys

def error():
    print("Error, ending program.")
    sys.exit()

def html():
    namethefile = input("INPUT THE NAME OF THE FILE \n")

    if os.path.isfile(namethefile+".html"):
        files = open(namethefile+".html","r+")
    else:
        files = open(namethefile+".html","x")
        files.close()
        files = open(namethefile+".html","r+")

    files.write("<!DOCTYPE html>\n <html>\n <style>\nheader {\n height: 200px; \nborder-spacing: 0px;\ntext-align: center;\n}\n footer {\n height: 50px; \nborder-spacing: 0px;\ntext-align: center;\n}\n</style>\n<header></header>\n<main></main>\n<footer></footer>\n</html>")

    files.close()


    print("File created")
def java():
    namethefile = input("INPUT THE NAME OF THE FILE \n")
    class_name = input("INPUT THE NAME OF THE CLASS")

    if os.path.isfile(namethefile+".java"):
        files = open(namethefile+".java","r+")
    else:
        files = open(namethefile+".java","x")
        files.close()
        files = open(namethefile+".java","r+")

    files.write("public class "+class_name+"{\n public static main(Str[]args){\n System.out.println('Hello World');}\n}")

    files.close()

    print("File created!")
def python():
    namethefile = input("INPUT THE NAME OF THE FILE \n")

    if os.path.isfile(namethefile+".py"):
        files = open(namethefile+".py","r+")
    else:
        files = open(namethefile+".py","x")
        files.close()
        files = open(namethefile+".py","r+")

    files.write("import random \nimport time \nimport tools as ts")

    files.close()

    print("File created!")
import webbrowser

def LookUp():
    ws = input("what would you like to lookup?\n")
    url_goog = 'https://www.google.com/search?q='
    lu = '+'.join((ws.split(' ')))
    print("Searching for "+ws)
    webbrowser.open(url_goog + lu)
    return LookUp
def repl():
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
        error()
