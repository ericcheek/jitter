#!/usr/bin/env python

import time
from datetime import datetime, timedelta
from dateutil import tz
import random
import sys
import math

from timebox import run_timebox
from notifier import notify, bell

def loop(duration, notification, randomize=False, repeat=False, progress=False):
    while True:
        sleeptime = duration
        if randomize:
            z = random.random()
            sleeptime = math.log(1-z)/(-1.0/duration)

        result = run_timebox(sleeptime, progress)

        if not result:
            break

        notification()

        if not repeat:
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s [-t] [-b] [-r] [-l] <duration seconds>" % sys.argv[0]
        print "-t : show toast"
        print "-b : bell sound"
        print "-r : randomize"
        print "-v : show progress"
        print "-l : loop"
        print "-w : wait (for beep process)"
        sys.exit(-1)

    # TODO: support formatted durations like 10m
    duration = int(sys.argv[-1])
    toast = '-t' in sys.argv
    sound = '-b' in sys.argv
    randomize = '-r' in sys.argv
    show_progress = '-v' in sys.argv
    repeat = '-l' in sys.argv
    beep_wait = "-w" in sys.argv

    def notification():
        if toast:
            #tod = datetime.now(tz.gettz('America/Los_Angeles')).strftime("%H:%M")
            tod = datetime.now().strftime("%H:%M")
            notify(tod)
        if sound:
            bell(beep_wait)

    try:
        loop(duration, notification, randomize, repeat, show_progress)
    except KeyboardInterrupt:
        print "terminating"
