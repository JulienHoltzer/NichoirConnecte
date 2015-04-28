#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import time
import datetime
import threading
import os
import csv

import nytumblr
import nysensors
import nygithub
import nydb

logger = logging.getLogger(__name__)

# stockage de la température toutes les N secondes
def stocke_temperature():
   threading.Timer(2.0, stocke_temperature).start()
   temp = nysensors.sensor_temp()
   nydb.sauve_temperatures(temp)

def stocke_poids():
   threading.Timer(10.0, stocke_poids).start()
   poids_nid = nysensors.sensor_weight_nest()
   poids_ref = nysensors.sensor_weight_ref()
   nydb.sauve_poids(poids_nid, poids_ref)

def publie_taille():
   taille = os.stat(nydb.chemin_dbfile()).st_size
   logging.info("La taille de la base est de %s octets." % taille)
   nytumblr.message("size","La base de données est à jour !","La taille de la base est de %s octets." % taille)
   threading.Timer(3600.0, publie_taille).start()

def publie_csv_jour():
   jour = datetime.datetime.today().date()
   csvfile = "/home/pi/NichoirConnecte/csv/%s.csv" % jour
   with open(csvfile,'wb') as f:
      writer = csv.writer(f)
      writer.writerow(['Jour','Heure','Donnée','Valeur'])
      data = nydb.liste_temperatures_jour()
      logger.debug(data)
      for row in data:
         writer.writerows(data)
      f.close()
   taille = os.stat(csvfile).st_size
   nytumblr.upload_csv_link(jour,taille)
   nygithub.upload_csv(csvfile,jour)
   # relance pour 24 heures
   threading.Timer(24*60*60.0, publie_csv_jour).start()


def stocke_commit():
   threading.Timer(10.0, stocke_commit).start()
   nydb.commit()

# lancement comme un module du Cube
def init(cube, params):
   logging.info("Lancement des boucles de stockage")
   stocke_temperature()
   stocke_poids()
   stocke_commit()
   publie_taille()
   publie_csv_jour()
