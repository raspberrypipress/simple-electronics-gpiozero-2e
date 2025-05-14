from gpiozero import OutputDevice, InputDevice
from time import sleep, time

def LDR_value(pin, charge_time_limit=0.005, min_readings=100):
    
    # Take the pin LOW to discharge the capacitor
    ldr = OutputDevice(pin=pin)
    ldr.off()
    sleep(0.1)
    ldr.close()

    # Configure the pin as a floating input
    ldr = InputDevice(pin=pin, pull_up=None, active_state=True)

    # Wait until the time limit for the capacitor to recharge 
    lit = 0
    start = time()
    while time() - start < charge_time_limit:
        if ldr.is_active:
            lit = 1
            break
    ldr.close()

    return lit

while True:
    print(LDR_value(4))
    sleep(1)  # Wait for a second
