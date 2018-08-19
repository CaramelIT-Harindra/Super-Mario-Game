from config import GRID_CONFIG


class Person:
    '''Characteristics of a person'''

    def __init__(self, name, height, width, speed):
        '''Contructor for person objects'''
        self.name = name
        self.height = height
        self.width = width
        self.speed = speed
        self.pos = {'x': 0, 'y': (GRID_CONFIG['HEIGHT'] - 1)}
        self.gravity = True
        self.surface = GRID_CONFIG['HEIGHT'] - 1
        self.base = GRID_CONFIG['ACTUAL_HEIGHT'] - 1
        self.max_jump = self.height * 2
        self.jump_from = self.base

    def move():
        pass
