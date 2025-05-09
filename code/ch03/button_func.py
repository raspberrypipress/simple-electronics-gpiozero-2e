from gpiozero import Button
from signal import pause

button = Button(21)

def button_pressed():
    print("Button was pressed")

button.when_pressed = button_pressed
pause()
