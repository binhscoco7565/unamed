import csv

flashcard = []

file = open("testing.csv", "r+", encoding="utf8", newline="")
result  = open("result.csv", "r+")
reader = csv.reader(result)
for i in reader:
    print(i)
    flashcard.append(i)
print(flashcard)
print(flashcard[0])
writer = csv.writer(file)
for i in range(2):  
    writer.writerow(flashcard[i])
# REMEBER TO CLOSE FILE
file.close()
result.close()