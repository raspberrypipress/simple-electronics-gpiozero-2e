from gpiozero import DistanceSensor
from gpiostepper import Stepper

sensor = DistanceSensor(echo=16, trigger=20)

# Steps per revolution and gear ratio
# from the 28BYJ-48 datasheet.
num_steps = 32
gear_ratio = 64
geared_steps = num_steps * gear_ratio

step_motor_l = Stepper(motor_pins=[14, 15, 18, 23],
                       number_of_steps=num_steps)
step_motor_r = Stepper(motor_pins=[19, 13, 5, 6],
                       number_of_steps=num_steps)

def move(direction='F', ctr=geared_steps):
    step_dir = 1 # 1 for fwd, -1 for back
    if direction == 'B':
        step_dir = -step_dir
    
    while ctr > 0: 
        if sensor.distance > .1: # move if no obstacles
            # F=fwd, B=back, L=left, R=right
            if direction in ['L', 'B', 'F']: 
                step_motor_l.step(step_dir)  # Left wheel only
            if direction in ['R', 'B', 'F']: 
                step_motor_r.step(-step_dir) # Right wheel only
            ctr -= 1

for i in range(4): # Draw a right-handed square
    move("F", geared_steps*2) # move forward two revolutions
    move("R", geared_steps)   # Turn right 1/2 revolution