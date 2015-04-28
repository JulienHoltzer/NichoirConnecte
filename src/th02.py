#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smbus
import time

bus = smbus.SMBus(1)

while 1:
    bus.write_byte_data(0x40, 0x03, 0x11)
    time.sleep(0.5)
    d1 = bus.read_byte_data(0x40, 0x01)
    d2 = bus.read_byte_data(0x40, 0x02)
    temp = float(((d2 | d1 << 8) >> 2) / 32.0 - 50)
    bus.write_byte_data(0x40, 0x03, 0x01)
    time.sleep(0.5)
    d1 = bus.read_byte_data(0x40, 0x01)
    d2 = bus.read_byte_data(0x40, 0x02)
    humid = float(((d2 | d1 << 8) >> 4) / 16.0 - 24)
    print "Temp: " + `temp` + "°C, Humidity: " + `humid` + "%"
    time.sleep(1)
