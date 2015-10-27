#!/usr/bin/env python
# -*- coding: utf8 -*-

import smbus
import time
import logging


from raspiomix import Raspiomix

r = Raspiomix()

bus = smbus.SMBus(1)

#
logger = logging.getLogger('Adafruit_BMP.BMP085')
logger.setLevel(logging.INFO)

logger = logging.getLogger('Adafruit_I2C.Device.Bus.1.Address.0X77')
logger.setLevel(logging.INFO)

def sensor_temp():
    return r.readAdc(1)

def sensor_lum():
    return r.readAdc(0)

# lecture du poids du nid (entrée analogique)
def sensor_weight_nest():
    return 0

# lecture du poids du nid (entrée analogique)
def sensor_weight_ref():
    return 0
