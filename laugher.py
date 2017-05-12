import os
import random

import gpiozero
from sh import mpg321

LAUGH_FILE = 'laugh_{}.mp3'
PIR = gpiozero.MotionSensor(14, queue_len=10, threshold=0.999)
ROOT_DIR = '/home/pi/pi-laugher/assets/audio'

while True:
    PIR.wait_for_motion()
    laugh_track = LAUGH_FILE.format(random.randint(1, 7))
    track_path = os.path.join(ROOT_DIR, laugh_track)

    mpg321(track_path)
