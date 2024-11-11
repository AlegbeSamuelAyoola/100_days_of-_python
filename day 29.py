import time

def text(colour, word):
  if colour == "Black":
    print('\033[30m', word, sep="", end="")
  elif colour == "Red":
    print("\033[31m", word, sep="", end="")
  elif colour == "Green":
    print("\033[32m", word, sep="", end="")
  elif colour == "Yellow":
    print("\033[33m", word, sep="", end="")
  elif colour == "Blue":
    print("\033[34m", word, sep="", end="")
  elif colour == "Magenta":
    print("\033[35m", word, sep="", end="")
  elif colour == "Cyan":
    print("\033[36m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("== Super Subroutine ==")
print()
time.sleep(1)
print("with my ", end="")
text("Magenta", "new program ")
text("Reset", "I can just call red ('and') ")
text("Red", "and ")
text("Reset", "that colour will appear in the colour I set it too.")
print()
time.sleep(1)
print()
print("With no ", end="")
text("Cyan", "weird gaps.")
print()
time.sleep(1)
print()
text("Reset", "Epic!")