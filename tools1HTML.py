import os.path
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

    
