#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import time
import datetime
import picamera
import threading

import nytumblr

camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True

# prise d'une photo toutes les 10 secondes
def publie_photo():
   logging.debug("Dites Ouistiti !")
   camera.capture('/home/pi/snapnichoir.jpg')
   nytumblr.snapshot("Et une nouvelle photo !",'/home/pi/snapnichoir.jpg')
   threading.Timer(10.0, publie_photo).start()



# lancement comme un module du Cube
def init(cube, params):
   logging.info("Prise de photo au lancement")
   publie_photo()
