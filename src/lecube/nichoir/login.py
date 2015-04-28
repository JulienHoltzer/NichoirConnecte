#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import time

import netifaces as ni

import nytumblr

try:
    adresse_eip = ni.ifaddresses('eth0')[2][0]['addr']
except ValueError:
    adresse_eip = "..."

try:
    adresse_wip = ni.ifaddresses('wlan0')[2][0]['addr']
except ValueError:
    adresse_wip = "..."


date = time.strftime('%d/%m/%y',time.localtime())
heure = time.strftime('%H:%M',time.localtime())


message = "D&eacute;marrage du nichoir le %s &agrave; %s sur adresse %s" % (date, heure, adresse_eip)

logging.info(message)


# lancement comme un module du Cube
def init(cube, params):
    logging.info("Start nichoir")
    nytumblr.message("booting", "Lancement de l'application", message)

