import sys
import termios
import tty
import os
import time
from config import FRAME_RATE


def keyAction(key=None, player=None, scene=None):
    if scene is None:
        return
    if player is None:
        return
    if key is None:
        player.showMe(scene=scene)
    else:
        if key == 'q':
            time.sleep(1/FRAME_RATE)
            return False
        elif key == 'a':
            player.showMe(action='LEFT', scene=scene)
            time.sleep(1/FRAME_RATE)
        elif key == 'd':
            player.showMe(action='RIGHT', scene=scene)
            time.sleep(1/FRAME_RATE)
        elif key == 'w':
            player.showMe(action='JUMP', scene=scene)
            time.sleep(1/FRAME_RATE)
        elif key == 'i':
            print("INSTRUCTIONS")
            time.sleep(1/FRAME_RATE)
            # INSTRUCTIONS
        elif key == 'p':
            print("PAUSE")
            time.sleep(1/FRAME_RATE)
        else:
            pass
            time.sleep(1/FRAME_RATE)
            # PAUSE
    return True
