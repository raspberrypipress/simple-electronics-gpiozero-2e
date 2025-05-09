from gpiozero import LED, Button
from time import sleep
from signal import pause
led = LED(25)
button = Button(21)

def button_pressed():
    led.on()

def button_released():
    sleep(3)
    led.off()

button.when_pressed = button_pressed
button.when_released = button_released
pause()
