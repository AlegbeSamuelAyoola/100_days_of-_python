import random,time

# Generate 8 unique random numbers
numbers = random.sample(range(1, 91), 8)

# Sort the numbers
numbers.sort()

bingo = "BINGO"

# Create the Bingo card with the "BINGO" in the center
bingocard = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], bingo, numbers[4]],
    [numbers[5], numbers[6], numbers[7]]
]

# Print the Bingo card with delays
print(f"{bingocard[0][0]}  |   {bingocard[0][1]}  |   {bingocard[0][2]}")
time.sleep(2)
print("------------------")
time.sleep(2)
print(f"{bingocard[1][0]}  | {bingocard[1][1]} |   {bingocard[1][2]}")
time.sleep(2)
print("------------------")
time.sleep(2)
print(f"{bingocard[2][0]}  |   {bingocard[2][1]}  |   {bingocard[2][2]}")
