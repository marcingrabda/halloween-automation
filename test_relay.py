#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

RELAY = 23

class Board:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)        
        GPIO.setup(RELAY, GPIO.OUT)

    def relay_on(self):
        GPIO.output(RELAY, 1)

    def relay_off(self):
        GPIO.output(RELAY, 0)

    def cleanup(self):
        GPIO.cleanup()

def sleep(seconds):
    time.sleep(seconds)

def main():
    board = Board()
    board.relay_on()
    sleep(3)
    board.relay_off()
    board.cleanup()

if __name__ == "__main__":
    main()