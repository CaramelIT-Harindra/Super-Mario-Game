from person import Person
from config import ENEMY_CONFIG


class Enemy(Person):
    '''Characteristics of an enemy'''

    def __init__(self, name="Enemy", height=None, width=None, speed=None):
        '''Contructor for enemy objects'''
        if name is None:
            name = "Enemy"
        if height is None:
            height = 1 * ENEMY_CONFIG['SIZE']
        if width is None:
            width = 1 * ENEMY_CONFIG['SIZE']
        if speed is None:
            speed = 1 * ENEMY_CONFIG['SIZE']
        super(Person, self).__init__(name, height, width, speed)
        self.lives = 1
        self.damage = 1
