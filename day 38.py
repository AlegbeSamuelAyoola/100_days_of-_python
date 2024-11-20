sentence = input("Type in any sentence >\n")

for letter in sentence:
    if letter.lower() == "b":
        print("\033[0;34m", end='') #blue
    elif letter.lower() == "r":
        print("\033[0;31m", end='') #red
    elif letter.lower() == "y":
        print("\033[1;33m", end='') #yellow
    elif letter.lower() == "g":
        print("\033[0;32m", end='') #green
    elif letter.lower() == " ":
        print("\033[0m", end='') #back to default
    print(letter, end="")
        