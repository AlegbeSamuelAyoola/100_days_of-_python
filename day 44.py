import random
import time
import os

print("Bingo Card Creator")
time.sleep(2)
os.system('cls')
time.sleep(1)
print("Creating Your Random Bingo Card Now")
time.sleep(2)
os.system('cls')
time.sleep(1)
print("Let's Play Bingo!")
print()

def randomNum():
  number = random.randint(1, 90)
  return number

def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t | \t ")
    print()
    
def createCard():
  global bingo
  numbers = []
  for i in range(8):
    num = randomNum()
    while num in numbers:
      num = randomNum()
    numbers.append(randomNum())
  
  numbers.sort()
  
  bingo = [ [numbers[0], numbers[1], numbers[2]],
            [numbers[3], "BG", numbers[4]], 
            [numbers[5], numbers[6], numbers[7]]
          ]

time.sleep(1)
createCard()

while True:
  prettyPrint()
  print()
  num = int(input("Next Number: "))
  for row in range(3):
    for item in range(3):
      if bingo[row][item] == num:
        print()
        time.sleep(1)
        bingo[row][item] = "X"
        print("You have that number!")
        print()
        time.sleep(1)

  crosses = 0
  for row in bingo:
    for item in row:
      if item == "X":
        crosses+=1

  if crosses == 8:
    print("You Have Won! BINGO!")
    break
  time.sleep(1)
  os.system('cls')