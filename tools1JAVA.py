import os.path
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
