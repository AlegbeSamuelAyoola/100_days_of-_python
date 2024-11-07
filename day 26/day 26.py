import winsound,time,os

def play():
    file_path = 'C:\\Users\\LEOVO\\Documents\\GitHub\\100_days_of-_python\\day 26\\Aaron Smith - Dancin (KRONO Remix).wav'
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

while True: 
        print("====== My Music Player ======")
        time.sleep(2)
        print("Press 1 to play")
        time.sleep(2)
        print("Press 2 to exit")
        time.sleep(2)
        print("Press any other thing to see the menu again")
        Q1 = input()

        if Q1 == "1":
              print("Playing...............")
              play()
        if Q1 == "2":
              os.system("cls")
              break
        else:
              os.system("cls")
              continue
