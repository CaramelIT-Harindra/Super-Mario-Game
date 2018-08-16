import config
import time
import os
import helpers
from colorama import Back, Fore, Style
from player import Player
from enemy import Enemy
from scene import Scene
from input import Get, input_to

GAME_PLAY = True

scene = Scene()
player = Player(name="Mario", height=None, width=None, speed=None)
getch = Get()

while GAME_PLAY:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.WHITE + "Score: {0}".format(player.score))
    scene.render(player=player)

    # key_pressed = None
    # key_pressed = helpers.detectKeyPress()
    key_pressed = input_to(getch, timeout=5000/config.FRAME_RATE)
    if key_pressed is not None:
        GAME_PLAY = helpers.keyAction(
            key=key_pressed.lower(), player=player, scene=scene)
    else:
        GAME_PLAY = helpers.keyAction(key=None, player=player, scene=scene)

    time.sleep(1/config.FRAME_RATE)
