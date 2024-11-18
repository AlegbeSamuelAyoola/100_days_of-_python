pnames = []

def fullname(firstname,lastname):
    fullname = firstname + " " + lastname
    return fullname

def printlist():
    for i in pnames:
        print(i)

while True:
    firstname = input("First Name: ").strip().capitalize()
    lastname = input("Last Name: ").strip().capitalize()
    print()
    if fullname(firstname,lastname) not in pnames:
        pnames.append(fullname(firstname,lastname))
        printlist()
        print()
    else:
        print("ERROR: DUPLICATE NAME")
        print()
        continue