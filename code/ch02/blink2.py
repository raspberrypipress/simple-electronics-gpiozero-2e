from gpiozero import LED
from signal import pause
red = LED(25)
red.blink()
pause()
