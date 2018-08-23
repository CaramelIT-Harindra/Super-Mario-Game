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

# scene = Scene(level=1)
score_level = []
scenes = [Scene(level=1), Scene(level=2), Scene(level=3)]
player = Player(name="Mario", height=None, width=None, speed=1)
# scene.createMe()
# player.createMe(scene=scene)
getch = Get()
result = False

os.system("aplay -q Sounds/start.wav &")

for i in range(0, config.NUM_LEVELS):
    result = False
    scene = scenes[i]
    scene.createMe()
    player.reset_pos()
    player.createMe(scene=scene)
    score_level.append(player.score)

    while GAME_PLAY:
        os.system('cls' if os.name == 'nt' else 'clear')

        new_score = (
            int(player.pos['x'] / (player.width * 2)) * 200) + score_level[i]
        if new_score > player.score:
            player.score = new_score

        print(Fore.WHITE +
              "\n\t\t\tScore: {0}\t\tLives: {1}\n".format(player.score, player.lives))

        scene.render(player=player)

        player.lives = config.PLAYER_CONFIG['START_LIVES'] - \
            config.PLAYER_CONFIG['LIVES_LOST']

        if player.lives <= 0:
            result = False
            break

        if player.pos['x'] > (scene.actual_width - config.PLAYER_CONFIG['SIZE'] - 5):
            result = True
            player.score += player.lives * 1000
            break

        if player.pos['y'] == player.base:
            result = False
            break

        scene.refresh(player=player)

        key_pressed = input_to(getch, timeout=5000/config.FRAME_RATE)
        if key_pressed is not None:
            GAME_PLAY = helpers.keyAction(
                key=key_pressed.lower(), player=player, scene=scene)
        else:
            GAME_PLAY = helpers.keyAction(key=None, player=player, scene=scene)
        # time.sleep(1/config.FRAME_RATE)
    if result == False:
        break

os.system("aplay -q Sounds/gameover.wav &")

if result is False:
    os.system('cls' if os.name == 'nt' else 'clear')

    new_score = int(player.pos['x'] / (player.width * 2)) * 200
    if new_score > player.score:
        player.score = new_score

    print(Fore.WHITE +
          "\n\t\t\tScore: {0}\t\tLives: {1}\n".format(player.score, player.lives))

    scene.render(player=player)

    print('\n\t\t\t\t  GAME OVER')
    print('\n\t\t\t\t Score: {0}\n'.format(player.score))
else:
    os.system('cls' if os.name == 'nt' else 'clear')

    new_score = int(player.pos['x'] / (player.width * 2)) * 200
    if new_score > player.score:
        player.score = new_score

    print(Fore.WHITE +
          "\n\t\t\tScore: {0}\t\tLives: {1}\n".format(player.score, player.lives))

    scene.render(player=player)

    print('\n\t\t\t\t  GAME OVER')
    print('\n\t\t\t\t   YOU WON')
    print('\n\t\t\t\t Score: {0}'.format(player.score))
