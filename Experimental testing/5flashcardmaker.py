import csv

card = []
flashcard = []

file = open("testing.csv", "r+", encoding="utf8", newline="")

writer = csv.writer(file)

for i in range(2):
    print(i)
    card = []
    front = input("front: ")
    back = input("back: ")
    card.append(front)
    card.append(back)
    print(card)
    flashcard.append(card)
    print(flashcard)
    writer.writerow(flashcard[i])


print(flashcard[1])
flashcard = []
print(flashcard)
file.close()