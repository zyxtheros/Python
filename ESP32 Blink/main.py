from machine import Pin # installed from pip install pyserial docopt python-dotenv adafruit-ampy
from time import sleep

led = Pin(19, Pin.OUT)


while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)