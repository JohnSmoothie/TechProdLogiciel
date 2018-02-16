import csv

tab = []
tab2 = []
with open('installation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        tab.append(row)


for col in tab[1] :
    print(col)
tabfin = []
cmp = 0

#utiliser sqlite pour les bd