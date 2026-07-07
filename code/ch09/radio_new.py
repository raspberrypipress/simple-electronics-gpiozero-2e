from gpiozero import MCP3008
from subprocess import Popen, run
import time

station_dial = MCP3008(0)
volume_dial = MCP3008(1)

url = "http://ice1.somafm.com/{0}"
Grooves = url.format("groovesalad-128-mp3")
Indie = url.format("indiepop-128-mp3")

current_station = None
vlc_process = None
last_volume = -1

def set_volume(vol_percent):
    volume = vol_percent / 100.0
    run(["wpctl", "set-volume", "@DEFAULT_AUDIO_SINK@", f"{volume:.2f}"])

def change_station(station_url):
    global vlc_process, current_station
    if station_url != current_station:
        print(f"Tuning to new station stream...")
        if vlc_process is not None:
            vlc_process.terminate()
            vlc_process.wait()  # Ensure the old stream closes cleanly
        vlc_process = Popen(["cvlc", "--no-video", station_url])
        current_station = station_url

try:
    while True: 
        # Read volume pot (maps 0.0-1.0 to 0%-100%)
        vol = int(volume_dial.value * 100)     
        if vol != last_volume:
            set_volume(vol)
            last_volume = vol
        
        # Read tuning pot
        if station_dial.value >= 0.5:
            target_station = Grooves
        else:
            target_station = Indie
            
        change_station(target_station)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nShutting down radio safely...")
    if vlc_process is not None:
        vlc_process.terminate()