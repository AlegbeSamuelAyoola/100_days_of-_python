import os,time,csv

total = 0.0

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 54"
file_path = os.path.join(folder_path, "Day54Totals.csv")

with open(file_path) as file:
    reader = csv.DictReader(file)
    for row in reader:
        cost = float(row["Cost"])
        quantity = int(row["Quantity"])
        value = (cost * quantity)
        total += value
        total = (round(total,2))
    
    print("calculating......")
    time.sleep(2)
    print(f"The shop makes ${total} in a day")
        