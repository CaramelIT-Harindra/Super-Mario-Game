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
player = Player(name="Mario", height=None, width=None, speed=2)
scene.createMe()
player.createMe(scene=scene)
getch = Get()
result = False

while GAME_PLAY:
    os.system('cls' if os.name == 'nt' else 'clear')

    new_score = int(player.pos['x'] / (player.width * 2)) * 200
    if new_score > player.score:
        player.score = new_score

    print(Fore.WHITE + "Score: {0}".format(player.score))

    scene.render(player=player)

    if player.pos['x'] > (scene.actual_width - config.PLAYER_CONFIG['SIZE'] - 5):
        result = True
        break

    if player.pos['y'] == player.base:
        result = False
        break

    key_pressed = input_to(getch, timeout=5000/config.FRAME_RATE)
    if key_pressed is not None:
        GAME_PLAY = helpers.keyAction(
            key=key_pressed.lower(), player=player, scene=scene)
    else:
        GAME_PLAY = helpers.keyAction(key=None, player=player, scene=scene)

    # time.sleep(1/config.FRAME_RATE)

if result is False:
    print('GAME OVER')
    print('Score: {0}'.format(player.score))
else:
    print('GAME OVER')
    print('YOU WON')
