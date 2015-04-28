
import os, sys
if not os.getuid() == 0:
    sys.exit('Needs to be root for running this script.')

import gaugette.ssd1306

import RPi.GPIO as GPIO

import time
import subprocess

# initialisation des boutons du boitier Yadom

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

led = gaugette.ssd1306.SSD1306(reset_pin=5, dc_pin=6, rows=64, cols=128)
led.begin()

print('Monitoring started')

while True:
    pressed = (GPIO.input(4) == 0)
    if pressed:
        time.sleep(4)
        pressed = (GPIO.input(4) == 0)
        if pressed:
            break
    else:
        time.sleep(0.1)

print('Shutdown button pressed. System is going to halt now')
led.clear_display()
led.draw_text2(16,16,"BYE !",4)
led.display()

subprocess.call('halt')

