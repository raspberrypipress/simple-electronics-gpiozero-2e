from gpiozero import OutputDevice, DigitalInputDevice
from time import sleep, time

def LDR_value(pin, charge_time_limit=0.003):
    
    # Take the pin LOW to discharge the capacitor
    ldr = OutputDevice(pin=pin)
    ldr.off()
    sleep(0.1)
    ldr.close()

    # Configure the pin as a floating input
    ldr = DigitalInputDevice(pin=pin, pull_up=None, 
                             active_state=True)

    # Wait until the time limit for the capacitor to recharge
    start = time()
    ldr.wait_for_active(timeout=charge_time_limit)

    # If the pin was active before the timeout, we have light
    elapsed = time() - start
    ldr.close()
    return elapsed < charge_time_limit

while True:
    print(LDR_value(4))
    sleep(1)  # Wait for a second