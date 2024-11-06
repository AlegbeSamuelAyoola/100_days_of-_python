import random

def n_sidesdice(n_sides):
    while True:
        n_roll = random.randint(1,n_sides)
        return n_roll
    
def multidice():
    while True:
        die1 = random.randint(1,6)
        die2 = random.randint(1,8)
        health = die1 * die2
        return health
             
print("====== Character Stats Generator ======")    

while True:
    health = multidice() 
    cname = input("Enter Warriors Name > ")
    print("The Warriors Health is",health,"hp")
    Q1 = input("Do you want to create another character? > ")
    if Q1 == "yes":
        continue
    else:
        print("Thank you for playing")
        break