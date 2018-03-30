#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, route, template, request, debug
import mysql.connector

app = Bottle()

conn = mysql.connector.connect(host="localhost",user="root",passwd="root",db="techprod",buffered=True)
cursor = conn.cursor()

@app.route('/resultat', method=['POST'])
def requete():
    activites = request.forms['activites']
    codeP = request.forms['codeP']
    select_stmt = "SELECT nomAct FROM activite WHERE nomAct=%(nomAct)s"
    #select_stmt = "SELECT nomAct,ville,codeP, FROM activite,installation WHERE activite.nomAct= %(nomAct)s and installation.codeP=%(codeP)s and installation.ville=activite.ville"
    #union select codeP from installation where codeP=%(codeP)s
    #, 'codeP' : codeP
    cursor.execute(select_stmt, {'nomAct' : activites})
    result = cursor.fetchall()
    cursor.close()
    return template('resultat.tpl', rows=result)


def requeteAct(nomAct):
    select_stmt = "SELECT nomAct FROM activite WHERE nomAct=%(nomAct)s"
    cursor.execute(select_stmt, {'nomAct' : nomAct})
    result = cursor.fetchall()
    cursor.close()



@app.route('/')
def accueil():
    return template('savetemp.tpl')

debug(True)
run(app, host='localhost',port='8080', debug=True, reloader=True)
