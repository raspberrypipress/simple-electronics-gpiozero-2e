import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()
samples = "/usr/share/sonic-pi/samples/"
drum = Sound(f"{samples}/drum_bass_soft.flac")
while True:
    drum.play()
