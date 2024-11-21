import random

listofwords = ["nigerian", "suave", "bald", "integrity", "good", "genius"]
letterchoosen = []
lives = 6
myword = random.choice(listofwords)

while True:
    letter = input("Enter a letter > ").lower()
    if letter in letterchoosen:
        print("You've picked that before")
        continue

    letterchoosen.append(letter)

    if letter in myword:
        print("You have found a letter")
    else:
        print("This letter is not present")
        lives -= 1

    allletters = True
    for i in myword:
        if i in letterchoosen:
            print(i, end="")
        else:
            print("_", end="")
            allletters = False
    print()

    if allletters:
        print(f"We have a winner! with {lives} lives left!")
        break

    if lives <= 0:
        print("You have run out of lives!")
        print(f"The answer was {myword}")
        break
    else:
        print(f"{lives} lives left!")
