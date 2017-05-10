import random

import gpiozero
from sh import mpg321

AUDIO_FILES = [
    './assets/audio/laugh_1.mp3',
    './assets/audio/laugh_2.mp3',
    './assets/audio/laugh_3.mp3',
    './assets/audio/laugh_4.mp3',
    './assets/audio/laugh_5.mp3',
    './assets/audio/laugh_6_short.mp3',
    './assets/audio/laugh_7.mp3'
    ]
PIR = gpiozero.MotionSensor(14, queue_len=10, threshold=0.999)

while True:
    PIR.wait_for_motion()
    print("Motion detected!")
    laugh_track = random.choice(AUDIO_FILES)
    mpg321(laugh_track)
