#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import pygame
import random

PIR_SENSOR = 11
RELAY = 23

class Board:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIR_SENSOR, GPIO.IN)
        GPIO.setup(RELAY, GPIO.OUT)

    def check_pir_sensor(self):
        return GPIO.input(PIR_SENSOR)

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
    print("Starting main loop...")
    try:
        while True:
            sleep(1)
            pir_triggered = board.check_pir_sensor()
            print(f"PIR: {pir_triggered}")
    except KeyboardInterrupt:
        print("Exiting...")
        pass
    finally:
        board.cleanup()

if __name__ == "__main__":
    main()
