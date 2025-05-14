import time, sys
from gpiozero import DistanceSensor, OutputDevice
from threading import Thread

sensor = DistanceSensor(echo = 16, trigger = 20)
IN1_m1 = OutputDevice(17)
IN2_m1 = OutputDevice(18)
IN3_m1 = OutputDevice(21)
IN4_m1 = OutputDevice(22)
step_pins_m1 = [IN1_m1,IN2_m1,IN3_m1,IN4_m1] # Motor 1 pins
IN4_m2 = OutputDevice(19)
IN3_m2 = OutputDevice(13)
IN2_m2 = OutputDevice(5)
IN1_m2 = OutputDevice(6)
step_pins_m2 = [IN1_m2,IN2_m2,IN3_m2,IN4_m2] # Motor 2 pins 
seq = [[1,0,0,1], # Define step sequence
       [1,0,0,0], # as shown in manufacturer's datasheet
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
step_count = len(seq)
all_clear = True
running = True

def bump_watch(): # thread to watch for obstacles
    global all_clear
    while running:
        value = sensor.distance
        if value < 0.1: # trigger if obstacle within 10cm
            all_clear = False
        else:
            all_clear = True

def move_bump(direction='F', seqsize=1, n_steps=2052):
    ctr = 0 # 2052 steps = 1 revolution for step size of 2
    step_dir = seqsize # 1 or 2 for fwd, -1 or -2 for back
    if direction == 'B':
        step_dir = step_dir * -1
    wait_time = 10/float(1000) # adjust this to change speed
    step_ctr = 0
    while all_clear and ctr < n_steps: # move if no obstacles
        for pin in range(0, 4):
            l_pin = step_pins_m1[pin]
            r_pin = step_pins_m2[pin]
            # F=fwd, B=back, L=left, R=right
            if seq[step_ctr][pin]!=0: 
                if direction in ['L', 'B', 'F']: 
                    l_pin.on() # Left wheel only
                if direction in ['R', 'B', 'F']: 
                    r_pin.on() # Right wheel only
            else: 
                l_pin.off()
                r_pin.off()
        step_ctr += step_dir
        if (step_ctr>=step_count): # Repeat sequence
            step_ctr = 0
        if (step_ctr<0):
            step_ctr = step_count+step_dir
        time.sleep(wait_time) # pause 
        ctr+=1

t1 = Thread(target=bump_watch) # run as separate thread
t1.start() # start bump watch thread
for i in range(4): # Draw a right-handed square
    move_bump('F',-2,4104)
    move_bump('R',-2,2052)
running = False
