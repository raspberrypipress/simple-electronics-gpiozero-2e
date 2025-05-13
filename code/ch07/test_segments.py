# Cycle through each segment in order
from gpiozero import LEDBoard
from time import sleep

#               a   b   c   d   e   f   g
seg = LEDBoard(17, 27, 24, 23, 22, 18, 25, active_high=False)

while True:
    for i in range(0, 7):
        print("abcdefg"[i])
        seg.on(i)
        sleep(1)
        seg.off(i)