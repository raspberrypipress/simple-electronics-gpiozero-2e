import pygame.mixer
from pygame.mixer import Sound
import os

pygame.mixer.init()
samples = "/usr/share/sonic-pi/samples/"
drum = Sound(os.path.join(samples, "drum_bass_soft.flac"))
while True:
    drum.play()