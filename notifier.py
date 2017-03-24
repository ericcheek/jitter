import os
import sys
import subprocess
import platform

DEVNULL = open(os.devnull, 'wb')

def notify(message):
    current_platform = platform.system()
    if current_platform == 'Darwin':
        p = subprocess.Popen(['terminal-notifier', '-message', message])
        p.wait()

    # TODO: support other platforms

def bell(wait=False):
    p = subprocess.Popen(['mpg123', '-q',
                          os.path.dirname(os.path.abspath(__file__)) + '/' + 'bowl_struck.mp3'],
                         #stdout=sys.stdout,
                         #stderr=sys.stderr
                         stdout=DEVNULL,
                         stderr=DEVNULL)

    if wait:
        p.wait()
