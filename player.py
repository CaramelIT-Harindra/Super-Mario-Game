from person import Person
from config import PLAYER_CONFIG


class Player(Person):
    '''Characteristics of a player'''

    def __init__(self, name="Mario", height=None, width=None, speed=None):
        '''Contructor for player objects'''
        if name is None:
            name = "Mario"
        if height is None:
            height = 1 * PLAYER_CONFIG['SIZE']
        if width is None:
            width = 1 * PLAYER_CONFIG['SIZE']
        if speed is None:
            speed = 1 * PLAYER_CONFIG['SIZE']
        super(Player, self).__init__(name, height, width, speed)
        self.lives = 5
        self.power = []
        self.ammo = []
        self.coins = 0
        self.score = 0
