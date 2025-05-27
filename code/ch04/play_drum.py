from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()
button = Button(2)
samples = "/usr/share/sonic-pi/samples/"
drum = Sound(f"{samples}/drum_bass_soft.flac")

button.when_pressed = drum.play
pause()
