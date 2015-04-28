#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import nytumblr

# appel des fonctions pour les entrées/sorties de la Raspberry Pi
import RPi.GPIO as GPIO

# pour compter le temps et lancer des programmes
import time
import subprocess

# nécessaire pour créer une boucle infinie
import threading

# la patte 4 est en entrée, par défaut à niveau haut (un appui met l'entrée à la masse)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def monitor_button():
    # on teste en permanence
    while True:
    	pressed = (GPIO.input(4) == 0)
	if pressed:
            # on a détecté l'appui sur le bouton, on compte 4 secondes
            time.sleep(4)
            pressed = (GPIO.input(4) == 0)
            if pressed:
                # le bouton est toujours pressé après 4 secondes : il faut éteindre
                # pour cela, on sort de la boucle infinie
                break
        else:
            # on met en pause le programme 
            time.sleep(0.1)

    # On va éteindre la carte, donc on prévient tout le monde
    logging.info('Arret du nichoir')

    nytumblr.message("halt", "Le nichoir s'éteint", "La carte électronique a été arrêtée par appui sur le bouton.")
   
    # On appelle le programme "halt" qui arrête le système d'exploitation
    # attention la carte restera sous tension, manipuler avec soin
    subprocess.call('halt')

# lancement comme un module du Cube
def init(cube, params):
    logging.info("Lancement du thread pour le bouton d'arrêt")
    threading.Thread(target=monitor_button).start()

