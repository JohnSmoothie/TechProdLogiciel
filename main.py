import csv

tab = []
tab2 = []
with open('installation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        tab.append(row)

print(tab[2])

#utiliser sqlite pour les bd