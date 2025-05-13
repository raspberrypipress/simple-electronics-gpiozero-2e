from gpiozero import OutputDevice, InputDevice
from time import sleep, time

def LDR_value(pin, charge_time_limit=0.005):
    
    # Take the pin LOW to discharge the capacitor
    ldr = OutputDevice(pin=pin, active_high=True, 
                       initial_value=False)
    sleep(0.1)

    # Configure the pin as an input
    ldr.close()
    ldr = InputDevice(pin=pin, pull_up=None,
                      active_state=True)

    # Wait for the capacitor to recharge, but only up to
    # the charge time limit
    lit = 0
    start = time()
    while True:
        if time() - start >  charge_time_limit:
            break
        if ldr.is_active:
            lit += 1

    ldr.close()
    print(lit)
    return lit > 5

while True:
    print(LDR_value(4))
    sleep(1)  # Wait for a second
