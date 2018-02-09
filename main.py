import csv

tab = []
with open('installation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tab.append(row)

print(tab)dddd
