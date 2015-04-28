#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import time
import datetime
import sqlite3

# définition de la base de données

dbfile = "/home/pi/NichoirConnecte/config/nichoir.db"

conn = sqlite3.connect(dbfile,detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False)


def sauve_temperatures(temp):
   conn.execute("""INSERT INTO temps VALUES (date('now'),time('now'),(?),(?))""",('interieur', temp))

def sauve_poids(poids_nid, poids_ref):
   conn.execute("""INSERT INTO poids VALUES (date('now'),time('now'),(?),(?))""",(poids_nid,poids_ref))

def chemin_dbfile():
   return dbfile

def liste_temperatures_jour():
   cur = conn.cursor()
   return cur.execute("SELECT * FROM temps WHERE tdate = date('now')").fetchall()

def liste_poids_heure():
   cur = conn.cursor()
   return cur.execute("SELECT ttime, poids_nid, poids_ref FROM poids WHERE ttime > time('now','-1 hour')").fetchall()

def commit():
   conn.commit()

def compteur_records():
   return conn.total_changes   
