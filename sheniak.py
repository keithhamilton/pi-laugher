import random

import gpiozero
from sh import afplay

AUDIO_FILES = [
    './assets/audio/laugh_1.mp3',
    './assets/audio/laugh_2.mp3',
    './assets/audio/laugh_3.mp3',
    './assets/audio/laugh_4.mp3',
    './assets/audio/laugh_5.mp3',
    './assets/audio/laugh_6_short.mp3',
    './assets/audio/laugh_7.mp3'
    ]
PIR = gpiozero.MotionSensor(4)

while True:
    if PIR.motion_detected:
        print("Motion detected!")
        laugh_track = random.choice(AUDIO_FILES)
        afplay(laugh_track)
