import time
import dbm
import datetime
import os

title = "Welcome to Tweeter"

def addTweet(db):
    tweet = input("Add Your Tweet: ")
    timeStamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    key = f"message{timeStamp}"
    db[key] = tweet
    time.sleep(1)
    os.system('cls')

def viewTweet(db):
    keys = sorted(db.keys(), reverse=True)
    counter = 0
    for key in keys:
        print(db[key].decode('utf-8'))
        print()
        time.sleep(0.5)
        counter += 1
        if counter % 10 == 0:
            nextTweets = input("Would you like to see the next 10 Tweets? (yes/no): ")
            print()
            if nextTweets.lower() == "no":
                break
    time.sleep(1)
    os.system('cls')

def deleteTweet(db):
    for key in db.keys():
        del db[key]
    print("Tweets have been cleared.")
    time.sleep(2)
    print()
    os.system('cls')

with dbm.open('tweet_db', 'c') as db:
    while True:
        print(f"{title:^60}")
        time.sleep(1)
        print()
        menu = input("What would you like to do?\n\n1: Add Tweet\n2: View Tweets\n3: Delete Tweets\n\nYour Option: ")
        print()
        if menu == "1":
            addTweet(db)
        elif menu == "2":
            viewTweet(db)
        elif menu == "3":
            deleteTweet(db)
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            time.sleep(2)
            os.system('cls')
