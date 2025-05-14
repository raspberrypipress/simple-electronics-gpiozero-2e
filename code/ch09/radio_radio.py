from gpiozero import MCP3008
from subprocess import Popen
import alsaaudio
import time

station_dial = MCP3008(0)
volume_dial = MCP3008(1)

url = "http://lstn.lv/bbcradio.m3u8?station={0}&bitrate={1}"
Music = url.format("bbc_6music", 96000)
Radio4 = url.format("bbc_radio_fourfm", 96000)
current_station = Radio4

vlc = None

def change_station(station):
    global current_station, vlc
    if station != current_station:
        if vlc is not None:
            vlc.terminate()
            vlc = None
        vlc = Popen(["cvlc", station])
        current_station = station

mixer = alsaaudio.Mixer()
while True:
    vol = int(65 + volume_dial.value * 35)
    mixer.setvolume(vol)
    if station_dial.value >= 0.5:
        station = Music
        change_station(station)
    elif station_dial.value < 0.5:
        station = Radio4
        change_station(station)
    time.sleep(0.1)