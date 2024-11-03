import random

print("====== Guess The Number Game ======")
print("Can you guess the correct Number?")
counter = 0
number = random.randint(1,1000000)
while True:
  guess_number = int(input("Make a Guess > "))
  if guess_number <  0:
    print("No negative numbers allowed!")
    exit()
  elif guess_number < number:
    counter += 1
    print("Number is too low, try again")
  elif guess_number > number:
    counter += 1
    print("Number is too high, try again")
    continue
  elif guess_number == number:
    print("You correctly guessed the number after",counter,"attempt(s)")
    print("Thank you for playing!")
    break
  else:
    print("Error")