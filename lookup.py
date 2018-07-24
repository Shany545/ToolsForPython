import webbrowser

def LookUp():
    ws = input("what would you like to lookup?\n")
    url_goog = 'https://www.google.com/search?q='
    lu = '+'.join((ws.split(' ')))
    print("Searching for "+ws)
    webbrowser.open(url_goog + lu)
    return LookUp
LookUp()
