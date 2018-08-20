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

    def move(self):
        pass

    def createMe(self, scene=None, code=None):
        if scene is None:
            return
        if code is None:
            return
        for i in range(self.pos['y'], self.pos['y'] - self.height, -1):
            for j in range(self.width):
                scene._grid[i][self.pos['x']+j] = code

    def clearMe(self, scene=None):
        if scene is None:
            return
        for i in range(self.pos['y'], self.pos['y'] - self.height, -1):
            for j in range(self.width):
                scene._grid[i][self.pos['x']+j] = GRID_CONFIG['CODE']['BLANK']

    def showMe(self, action=None, scene=None):
        if scene is not None:
            self.clearMe(scene=scene)
            if action is not None:
                self.move(action=action, scene=scene)
            else:
                self.move(scene=scene)
            self.createMe(scene=scene)

    def check_surround(self, scene=None, pos=None):
        for i in range(pos['y'], pos['y'] - self.height, -1):
            for j in range(self.width):
                if (scene._grid[i][pos['x']+j] != GRID_CONFIG['CODE']['BLANK'] and scene._grid[i][pos['x']+j] != GRID_CONFIG['CODE']['CLOUD'] and scene._grid[i][pos['x']+j] != GRID_CONFIG['CODE']['EXIT'] and scene._grid[i][pos['x']+j] != GRID_CONFIG['CODE']['GRASS']) or scene._grid[i][pos['x']+j] == GRID_CONFIG['CODE']['PLAYER']:
                    self.check_clash(scene=scene, y=i, x=pos['x']+j)
                    return False
        return True

    def check_clash(self, scene=None, y=None, x=None):
        if self.name == 'Mario':
            if scene._grid[y][x] == GRID_CONFIG['CODE']['ENEMY']:
                self.lives -= 1
        elif self.name == 'Enemy':
            return
