import csv
import mysql.connector

tab = []
with open('installation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        truc0 = row.pop(0)#nom
        truc1 = row.pop(1)#ville
        truc2 = row.pop(2)#code postale
        truc4 = row.pop(4)#nom rue
        tab2 = [truc0, truc1, truc2, truc4]
        tab.append(tab2)


for col in tab[1] :
    print(col)

cnx = mysql.connector.connect(user='E164572H', password='E164572H',host='infoweb',database='E164572H')
cursor = cnx.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement (
    nom varchar(50) DEFAULT NULL,
    ville varchar(50) DEFAULT NULL,
    codeP int(5) NOT NULL AUTO_INCREMENT,
    rue varchar(50) DEFAULT NULL,
    PRIMARY KEY(nom)
);
""")
cnx.close()
