# displays the distance in decimetres on a 7-segment display
from gpiozero import LEDBoard  , DistanceSensor
from time import sleep

seg = LEDBoard(17, 27, 24, 23, 22, 18, 25, active_high=False)
sensor = DistanceSensor(echo=15, trigger=4)

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

print("Display distance on a 7-seg display")
while True:
    distance = sensor.distance * 10 # distance in decimeters
    print("distance", distance)
    if distance > 15:
        distance = 15
    seg.value = seg_patterns[int(distance)]
    sleep(0.8)