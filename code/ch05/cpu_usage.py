from gpiozero import RGBLED
import psutil, time

led = RGBLED(14, 15, 18)

while True:
    cpu = psutil.cpu_percent()
    r = cpu / 100.0
    g = (100 - cpu)/100.0
    b = 0
    led.color = (r, g, b)
    time.sleep(0.1)