from gpiozero import LEDBoard
from time import sleep

seg = LEDBoard(17, 27, 24, 23, 22, 18, 25, active_high=False)

seg_patterns = [
    (1, 1, 1, 1, 1, 1, 0),
    (0, 1, 1, 0, 0, 0, 0),
    (1, 1, 0, 1, 1, 0, 1),
    (1, 1, 1, 1, 0, 0, 1),
    (0, 1, 1, 0, 0, 1, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (1, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 0, 1, 1),
    (1, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 1, 1, 1, 1),
    (1, 0, 0, 1, 1, 1, 0),
    (0, 1, 1, 1, 1, 0, 1),
    (1, 0, 0, 1, 1, 1, 1),
    (1, 0, 0, 0, 1, 1, 1),
]

while True:
    for i in range(0, 16):
        print(hex(i))
        seg.value = seg_patterns[i]
        sleep(1)
