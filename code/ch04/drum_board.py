from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause
import os

pygame.mixer.init()
samples = "/usr/share/sonic-pi/samples/"
sound_pins = {
    2: "drum_bass_soft.flac",
    3: "drum_cowbell.flac",
}
buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
    file = sound_pins[button.pin.number]
    sound = Sound(os.path.join(samples, file))
    button.when_pressed = sound.play
pause()