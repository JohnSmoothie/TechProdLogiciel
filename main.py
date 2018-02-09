import csv

tab = []
tab2 = []
with open('installation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        for attribut in row:
            tab2.append(attribut)
        tab.append(tab2)

print(tab)dddd
