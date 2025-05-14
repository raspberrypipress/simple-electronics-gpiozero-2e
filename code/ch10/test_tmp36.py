from gpiozero import MCP3008
from time import sleep

def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

adc = MCP3008(channel=7)
for temp in convert_temp(adc.values):
    print(f"The temperature is {temp}C")
    sleep(1)