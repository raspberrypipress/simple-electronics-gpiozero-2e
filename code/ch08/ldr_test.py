from gpiozero import OutputDevice, DigitalInputDevice
from time import sleep

def LDR_value(pin, charge_time_limit=0.001):
    
    # Take the pin LOW to discharge the capacitor
    ldr = OutputDevice(pin=pin)
    ldr.off()
    sleep(0.1)
    ldr.close()

    # Configure the pin as a floating input
    ldr = DigitalInputDevice(pin=pin, pull_up=None, 
                             active_state=True)

    # If the pin goes active before the timeout, we have light
    lit = ldr.wait_for_active(timeout=charge_time_limit)
    ldr.close()

    return lit

while True:
    print(LDR_value(4))
    sleep(1)  # Wait for a second