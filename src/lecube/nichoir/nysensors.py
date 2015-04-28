#!/usr/bin/env python
# -*- coding: utf8 -*-

import smbus
import time
import logging

import Adafruit_BMP.BMP085 as BMP085

from raspiomix import Raspiomix

r = Raspiomix()

# première lecture à vide des jauges de contrainte
zero_weight_nest = r.readAdc(0)
zero_weight_ref = r.readAdc(1)

bus = smbus.SMBus(1)

sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

#
logger = logging.getLogger('Adafruit_BMP.BMP085')
logger.setLevel(logging.INFO)

logger = logging.getLogger('Adafruit_I2C.Device.Bus.1.Address.0X77')
logger.setLevel(logging.INFO)

def sensor_temp():
    return sensor.read_temperature()


def sensor_temp_ext():
    bus.write_byte_data(0x40, 0x03, 0x11)
    time.sleep(0.05)
    d1 = bus.read_byte_data(0x40, 0x01)
    d2 = bus.read_byte_data(0x40, 0x02)
    temp = float(((d2 | d1 << 8) >> 2) / 32.0 - 50)
    return temp

def sensor_humid_ext():
    bus.write_byte_data(0x40, 0x03, 0x01)
    time.sleep(0.05)
    d1 = bus.read_byte_data(0x40, 0x01)
    d2 = bus.read_byte_data(0x40, 0x02)
    humid = float(((d2 | d1 << 8) >> 4) / 16.0 - 24)
    return humid

def sensor_lum():
    return r.readAdc(2)

# lecture du poids du nid (entrée analogique)
def sensor_weight_nest():
    return r.readAdc(0) - zero_weight_nest

# lecture du poids du nid (entrée analogique)
def sensor_weight_ref():
    return r.readAdc(1) - zero_weight_ref
