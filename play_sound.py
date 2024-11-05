#!/usr/bin/env python

import os
import pygame
import random

def load_sounds():
    pygame.mixer.init()
    files = os.listdir("sounds")
    sounds = list(map(lambda file: pygame.mixer.Sound(f"sounds/{file}"), files))
    return sounds

def play_sound(sounds):
    return random.choice(sounds).play()

def wait_to_finish(playing):
    while playing.get_busy():
        pygame.time.delay(100)

def main():
    print("Playing random sound file...")
    sounds = load_sounds()
    playing = play_sound(sounds)
    wait_to_finish(playing)

if __name__ == "__main__":
    main()