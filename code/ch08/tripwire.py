from gpiozero import OutputDevice, DigitalInputDevice, Buzzer
from time import sleep

def LDR_value(pin, charge_time_limit=0.001):
    ldr = OutputDevice(pin=pin)
    ldr.off()
    sleep(0.1)
    ldr.close()

    ldr = DigitalInputDevice(pin=pin, pull_up=None, 
                             active_state=True)
    lit = ldr.wait_for_active(timeout=charge_time_limit)
    ldr.close()

    return lit

buzzer = Buzzer(17)
ldr_pin = 4
while True:
    if LDR_value(ldr_pin):
        buzzer.beep(0.5, 0.5, n=8, background=False)
    sleep(0.1)