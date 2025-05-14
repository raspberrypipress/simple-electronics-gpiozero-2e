from gpiozero import Buzzer
from signal import pause

buzzer = Buzzer(17)
buzzer.beep()
pause()