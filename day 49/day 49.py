import os

folder_path = r"C:\Users\LEOVO\Documents\GitHub\100_days_of-_python\day 49"
file_path = os.path.join(folder_path, "high.score")
f = open(file_path, "r")


contents = f.readlines()

names = []
scores = []
for line in contents:
    parts = line.strip().split()
    if len(parts) == 2 and parts[1].isdigit() and parts[0].isprintable():
        names.append(parts[0])
        scores.append(int(parts[1]))

if names and scores:
    max_scores = max(scores)
    max_index = scores.index(max_scores)
    highname = names[max_index]
    print("The highest score is:", highname,max_scores)
else:
    print("no scores found in the file")