from config import GRID_CONFIG


class Person:
    '''Characteristics of a person'''

    def __init__(self, name, height, width, speed):
        '''Contructor for person objects'''
        self.name = name
        self.height = height
        self.width = width
        self.speed = speed
        self.pos = {'x': 0, 'y': (GRID_CONFIG['HEIGHT']-1)}
        self.gravity = True
        self.base = GRID_CONFIG['HEIGHT']-1
        self.max_jump = self.height * 4
        self.jump_from = self.base

    def move(self, action=None, scene=None):
        '''Function to handle movement of the person'''
        try:
            # if action is None:
            #     raise AttributeError
            # elif scene is None:
            #     raise AttributeError
            if scene is None:
                raise AttributeError
            if self.pos['y'] < self.base and action == 'JUMP'and (scene._grid[self.pos['y']+1][self.pos['x']] != GRID_CONFIG['CODE']['OBSTACLE']):
                return
            elif self.pos['x'] == 0 and action == 'LEFT':
                raise IndexError
            elif self.pos['x'] == (GRID_CONFIG['WIDTH']-1) and action == 'RIGHT':
                raise IndexError
            else:
                if action == 'LEFT':
                    self.pos['x'] = self.pos['x'] - (1 * self.width)
                elif action == 'RIGHT':
                    self.pos['x'] = self.pos['x'] + (1 * self.width)
                elif action == 'JUMP':
                    self.jump_from = self.base - self.pos['y']
                    self.gravity = False
                    self.pos['y'] = self.pos['y'] - 1
                else:
                    pass

                if (self.pos['y'] < self.base) and self.gravity and (scene._grid[self.pos['y']+1][self.pos['x']] != GRID_CONFIG['CODE']['OBSTACLE']):
                    self.pos['y'] = self.pos['y'] + (1 * self.height)
                if (not self.gravity) and ((self.base - self.jump_from - self.max_jump) != self.pos['y']) and action != 'JUMP'and (scene._grid[self.pos['y']-1][self.pos['x']] != GRID_CONFIG['CODE']['OBSTACLE']):
                    self.pos['y'] = self.pos['y'] - 1
                elif (not self.gravity) and ((self.base - self.jump_from - self.max_jump) == self.pos['y']) and action != 'JUMP':
                    self.gravity = True

                if (not self.gravity) and ((self.base - self.jump_from - self.max_jump) != self.pos['y']) and action != 'JUMP'and (scene._grid[self.pos['y']-1][self.pos['x']] == GRID_CONFIG['CODE']['OBSTACLE']):
                    self.gravity = True
        except(IndexError, AttributeError):
            return
