import json
import mysql.connector
import sqlite3
import traceback

# liens pour les fichiers :
# http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-installations/
# http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-fiches-equipements/
# http://data.paysdelaloire.fr/donnees/detail/equipements-sportifs-espaces-et-sites-de-pratiques-en-pays-de-la-loire-activites-des-fiches-equ/


def connexionBD() :
    global cnx
    try :
        cnx = mysql.connector.connect(user='E164572H', password='E164572H', host='infoweb', database='E164572H')
    except :
        print("Erreur de connexion à la base de donnée")
    return cnx

def suprimerTables() :
    global cnx
    cursor = cnx.cursor()
    try :
        cursor.execute("DROP TABLE activite")
    except :
        print("la table activite n'existe pas")
    try :
        cursor.execute("DROP TABLE equipement")
    except :
        print("la table equipement n'existe pas")
    try :
        cursor.execute("DROP TABLE installation")
    except :
        print("la table installation n'existe pas")
    cnx.commit()

def creerTables() :
    global cnx
    cursor = cnx.cursor()
    try :
        cursor.execute("CREATE TABLE IF NOT EXISTS activite(actId int(10) DEFAULT NULL, nomAct varchar(1000) DEFAULT NULL, ville varchar(100) DEFAULT NULL, nivAct varchar(40) DEFAULT NULL, equId int(10) DEFAULT NULL);")

        cursor.execute("CREATE TABLE IF NOT EXISTS equipement(equId int(20) DEFAULT NULL, nomEqu varchar(100) DEFAULT NULL, ville varchar(100) DEFAULT NULL, douche BOOLEAN DEFAULT NULL, ouvertSaison BOOLEAN DEFAULT NULL, longitude float(10) DEFAULT NULL, latitude float(10) DEFAULT NULL, type varchar(100), instId int(15) DEFAULT NULL);")
        cursor.execute("CREATE TABLE IF NOT EXISTS installation(instId int(20) DEFAULT NULL, nomInst varchar(100) DEFAULT NULL, ville varchar(100) DEFAULT NULL, codeP int(5) DEFAULT NULL, rue varchar(100) DEFAULT NULL, numVoie int(5) DEFAULT NULL, longitude float(10) DEFAULT NULL, latitude float(10) DEFAULT NULL, nbPlacePK int(10) DEFAULT NULL, PRIMARY KEY(instId));")
        print("truc")
    except :
        print("Erreur lors de la création des tables")
    cnx.commit()

def insererTableEquipement() :
    global cnx
    cursor = cnx.cursor()
    datastore = json.load(open("data.equipement.paysdelaloire.fr.json"))
    size = int(datastore["nb_results"])
    for i in range(0, size) :
        equId = datastore["data"][i]["EquipementId"]
        nomEqu = datastore["data"][i]["EquNom"]
        ville = datastore["data"][i]["ComLib"]
        if(datastore["data"][i]["EquDouche"] == "Non") :
            douche = False
        else :
            douche = True
        if(datastore["data"][i]["EquOuvertSaison"] == "Non") :
            ouvertSaison = False
        else :
            ouvertSaison = True
        longitude = datastore["data"][i]["EquGpsX"]
        latitude = datastore["data"][i]["EquGpsY"]
        type = datastore["data"][i]["EquipementTypeLib"]
        instId = datastore["data"][i]["InsNumeroInstall"]

        query = "INSERT INTO equipement(equId, nomEqu, ville, douche, ouvertSaison, longitude, latitude, type, instId) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        args = (equId, nomEqu, ville, douche, ouvertSaison, longitude, latitude, type, instId)
        cursor.execute(query, args)
    cnx.commit()



def insererTableActivite() :
    global cnx
    cursor = cnx.cursor()
    datastore = json.load(open("data.activites.paysdelaloire.fr.json"))
    size = int(datastore["nb_results"])

    for i in range(0, size) :
        actId = datastore["data"][i]["ActCode"]
        nomAct = datastore["data"][i]["ActLib"]
        ville = datastore["data"][i]["ComLib"]
        nivAct = datastore["data"][i]["ActNivLib"]
        equId = datastore["data"][i]["EquipementId"]

        query = "INSERT INTO activite(actId, nomAct, ville, nivAct, equId) VALUES(%s, %s, %s, %s, %s);"
        args = (actId, nomAct, ville, nivAct, equId)
        cursor.execute(query, args)
    cnx.commit()

def insererTableInstallation() :
    global cnx
    cursor = cnx.cursor()
    datastore = json.load(open("data.installation.paysdelaloire.fr.json"))

    size = int(datastore["nb_results"])

    for i in range(0, size) :
        id = datastore["data"][i]["InsNumeroInstall"]
        ville = datastore["data"][i]["ComLib"]
        nom = datastore["data"][i]["geo"]["name"]
        codeP = datastore["data"][i]["InsCodePostal"]
        rue = datastore["data"][i]["InsLibelleVoie"]
        numVoie = datastore["data"][i]["InsNoVoie"]
        longitude = datastore["data"][i]["Longitude"]
        latitude = datastore["data"][i]["Latitude"]
        nbPlacePK = datastore["data"][i]["InsNbPlaceParking"]

        query = "INSERT INTO installation(instId, nomInst, ville, codeP, rue, numVoie, longitude, latitude, nbPlacePK) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        #print(id, nom, ville, codeP, rue, numVoie, longitude, latitude, nbPlacePK)
        args = (id, nom, ville, codeP, rue, numVoie, longitude, latitude, nbPlacePK)
        cursor.execute(query, args)
    cnx.commit()

connexionBD()
suprimerTables()
creerTables()

insererTableActivite()
insererTableInstallation()
insererTableEquipement()
