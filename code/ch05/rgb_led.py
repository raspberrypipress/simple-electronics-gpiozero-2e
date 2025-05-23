from gpiozero import RGBLED
from time import sleep

led = RGBLED(14, 15, 18)

led.red = 1 # full red
sleep(1)
led.red = 0.5 # half red
sleep(1)
led.color = (0, 1, 0) # full green
sleep(1)
led.color = (1, 0, 1) # magenta
sleep(1)
led.color = (1, 1, 0) # yellow
sleep(1)
led.color = (0, 1, 1) # cyan
sleep(1)
led.color = (1, 1, 1) # white
sleep(1)
led.color = (0, 0, 0) # off
sleep(1)
# slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)
