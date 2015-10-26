#!/usr/bin/env python
# -*- coding: utf8 -*-

import nysensors
import nytumblr
import nydb

import logging
import threading
import json
import time
import datetime
import plotly.plotly as ply
from plotly.graph_objs import *

with open('/home/pi/NichoirConnecte/config/plotly.json') as config_file:
    plotly_user_config = json.load(config_file)

logger = logging.getLogger(__name__)

ply.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = ply.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 5000
        }
    }], filename='Nichoir du CIV')

logger.debug("Le graphe est disponible ici : %s" % url)
nytumblr.message("graphe", "Courbe de température", "Vous pouvez consulter la courbe des températures ici : %s" % url.encode('utf8'))

stream = ply.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

def publie_graphe_poids_heure():
   # relance pour 1 heure
   threading.Timer(3600.0, publie_graphe_poids_heure).start()
   # construction d'un graphe
   resultat = nydb.liste_poids_heure()
   abscisse = [item[0] for item in resultat]
   poids0 = Scatter(x=abscisse, y=[item[1] for item in resultat])
   poids1 = Scatter(x=abscisse, y=[item[2] for item in resultat])
   data = Data([poids0, poids1])
   url = ply.plot(data, filename='Derniers poids')

   # génération d'une image
   nytumblr.message("poids", "Les derniers poids", "Dispo ici : %s" % url.encode('utf8'))

   # envoi de l'image sur Tumblr



def publie_graphe_temp_live():
   # relance pour 10 seconde
   threading.Timer(10.0, publie_graphe_temp_live).start()
   #
   sensor_data = nysensors.sensor_temp()
   stream.write({'x': datetime.datetime.now(),'y': sensor_data})

# lancement comme un module du Cube
def init(cube, params):
   publie_graphe_poids_heure()
   publie_graphe_temp_live()
	

