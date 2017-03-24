#!/usr/bin/env python

import time
from datetime import datetime, timedelta
import math
import sys
import notifier

def redraw_progress(progress, size=30):
    sys.stdout.write('\r' + ' ' * (size + 10))

    complete = int(math.floor(progress * size))
    remaining = (size - complete) + 1
    sys.stdout.write('\r' + ('-' * complete) + '>' + (' ' * remaining))
    if progress < 1.0:
        sys.stdout.write('%.2f' % progress)
    sys.stdout.flush()

def run_timebox(duration=20*60, showProgress=False):
    target_time = datetime.utcnow() + timedelta(seconds=duration)
    while True:
        current_time = datetime.utcnow()
        if current_time > target_time:
            break

        progress = 1.0 - (target_time - current_time).seconds / float(duration)
        if showProgress:
            redraw_progress(progress)

        try:
            time.sleep(1)
        except:
            return False

    return True


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print "Usage: %s [-q] <duration>" % sys.argv[0]
        sys.exit(-1)

    notification = None if '-q' in sys.argv else lambda: notifier.notify("Timebox closed")
    duration = int(sys.argv[-1]) * 60

    start_time = datetime.utcnow()
    if run_timebox(duration, notification):
        if notification != None:
            notification()
        print "Complete\n"
    else:
        time_delta = datetime.utcnow() - start_time
        minutes, seconds = divmod(time_delta.seconds, 60)

        print "\nInterrupted after %d:%02d\n" % (minutes, seconds)

    # record total time
    # record debrief notes
    # ? pause/resume
