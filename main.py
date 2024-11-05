#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
import time
import pygame
import random
from datetime import datetime

PIR_SENSOR = 11
RELAY = 23

class Board:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIR_SENSOR, GPIO.IN)
        GPIO.setup(RELAY, GPIO.OUT)

    def check_pir_sensor(self):
        return GPIO.input(PIR_SENSOR) == 1

    def relay_on(self):
        GPIO.output(RELAY, 1)

    def relay_off(self):
        GPIO.output(RELAY, 0)

    def cleanup(self):
        GPIO.cleanup()

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        files = os.listdir("sounds")
        self.sounds = list(map(lambda file: pygame.mixer.Sound(f"sounds/{file}"), files))        

    def play_random_sound(self):
        playing = random.choice(self.sounds).play()
        while playing.get_busy():
            pygame.time.delay(100)

def sleep(seconds):
    time.sleep(seconds)

def main():
    board = Board()
    sounds = Sounds()
    print("Starting main loop...")
    try:
        while True:
            sleep(0.1)
            pir_triggered = board.check_pir_sensor()
            if pir_triggered == True:
                print("Motion detected at:", datetime.now())
                board.relay_on()
                sounds.play_random_sound()
                sleep(3)
                board.relay_off()
    except KeyboardInterrupt:
        print("Exiting...")
        pass
    finally:
        board.cleanup()

if __name__ == "__main__":
    main()
