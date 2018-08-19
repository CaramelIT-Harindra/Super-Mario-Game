from config import GRID_CONFIG, PLAYER_CONFIG
from colorama import Fore, Back, Style, init
from random import randint

# init(autoreset=True)


class Scene:
    '''Characteristics of game screen'''

    def __init__(self):
        '''Contructor for game screen'''
        self.height = GRID_CONFIG['HEIGHT']
        self.width = GRID_CONFIG['WIDTH']
        self.actual_width = GRID_CONFIG['ACTUAL_WIDTH']
        self.actual_height = GRID_CONFIG['ACTUAL_HEIGHT']
        self.window_left = 0
        self.window_right = GRID_CONFIG['WIDTH'] - 1
        self._grid = [[GRID_CONFIG['CODE']['BLANK']]
                      * self.actual_width for n in range(self.height+2)]
        self.grass_pos = []
        self.numGrass = 15
        self.pit_pos = []
        self.numPits = 4
        self.cloud_pos = []
        self.cloud_height = []
        self.numClouds = 4
        self.obs_height = []
        self.obs_pos = []
        self.numObs = 4

    def render(self, player=None, enemies=None):
        if player is None:
            return
        else:
            self.applyGrass()
            self.applyExitPipe()
            for row in range(self.actual_height):
                for col in range(self.window_left, self.width+self.window_left, 1):
                    if self._grid[row][col] == GRID_CONFIG['CODE']['BLANK']:
                        print(Back.LIGHTCYAN_EX + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['PLAYER']:
                        print(Back.RED + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['CLOUD']:
                        print(Back.WHITE + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['ENEMY']:
                        pass    # Print ENEMY
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['OBSTACLE']:
                        print(Back.LIGHTBLACK_EX + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['EXIT']:
                        print(Back.LIGHTBLUE_EX + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['GRASS']:
                        print(Back.GREEN + " ", end='')
                    else:
                        self._grid[row][col] = 0
                        print(Back.GREEN + " ", end='')
                print(Back.RESET + '')

    def createMe(self):
        self.createSurface()
        self.createClouds()
        self.createPits()
        self.createGrass()
        self.createObstacles()
        self.applyExitPipe()

        offset = 4
        for h in range(5, self.height - 10, 2):
            for i in range(5):
                self._grid[self.height -
                           h][offset+i] = GRID_CONFIG['CODE']['OBSTACLE']
            offset += 8

        for h in range(self.height - 10, 3, -2):
            for i in range(5):
                self._grid[h][offset+i] = GRID_CONFIG['CODE']['OBSTACLE']
            offset += 8

    def createSurface(self):
        for i in range(self.height, self.actual_height, 1):
            for j in range(self.actual_width):
                self._grid[i][j] = GRID_CONFIG['CODE']['OBSTACLE']

    def createPits(self):
        max_x = PLAYER_CONFIG['SIZE']
        x_pos = max_x

        for i in range(self.numPits):
            if i == 0:
                x_pos = randint(max_x + 1, max_x + 101)
            else:
                x_pos = randint(max_x + 10, max_x + 110)
            max_x = x_pos
            self.pit_pos.append(x_pos)
        self.applyPits()

    def applyPits(self):
        for i in range(self.numPits):
            for j in range(self.height, self.actual_height, 1):
                for k in range(0, 10 - 1, 1):
                    self._grid[j][k + self.pit_pos[i]
                                  ] = GRID_CONFIG['CODE']['BLANK']

    def createObstacles(self):
        max_x = PLAYER_CONFIG['SIZE']
        x_pos = max_x
        count = 0
        flag = True

        while count < self.numObs:
            flag = True
            if count == 0:
                x_pos = randint(max_x + 3, max_x + 101)
            else:
                x_pos = randint(max_x + 25, max_x + 125)
            for i in range(0, 10, 1):
                if self._grid[self.actual_height - 1][x_pos + i] == GRID_CONFIG['CODE']['BLANK']:
                    flag = False
                    break
            if flag is True:
                count += 1
                max_x = x_pos
                self.obs_pos.append(x_pos)
            else:
                continue

            obs_h = randint(4, 6)
            self.obs_height.append(obs_h)
        self.applyObs()

    def applyObs(self):
        for count in range(self.numObs):
            for j in range(self.height - self.obs_height[count-1], self.height, 1):
                for k in range(0, 7, 1):
                    self._grid[j][k + self.obs_pos[count-1]
                                  ] = GRID_CONFIG['CODE']['OBSTACLE']

    def applyExitPipe(self):
        for i in range(self.height - 5, self.height - 1, 1):
            for j in range(self.actual_width - 8, self.actual_width, 1):
                self._grid[i][j] = GRID_CONFIG['CODE']['EXIT']
        for i in range(4, 9, 1):
            self._grid[self.height - 6][self.actual_width -
                                        i] = GRID_CONFIG['CODE']['EXIT']
            self._grid[self.height - 1][self.actual_width -
                                        i] = GRID_CONFIG['CODE']['EXIT']

    def createClouds(self):
        max_x = PLAYER_CONFIG['SIZE']
        x_pos = max_x

        for i in range(self.numClouds):

            if i == 0:
                x_pos = randint(max_x + 1, max_x + 101)
            else:
                x_pos = randint(max_x + 10, max_x + 110)
            if x_pos > max_x:
                max_x = x_pos
            self.cloud_pos.append(x_pos)

            self.cloud_height.append(randint(2, 6))
        self.applyClouds()

    def applyClouds(self):
        for i in range(self.numClouds):
            for j in range(0, 3, 1):
                for k in range(0, 10 - 1, 1):
                    self._grid[j + self.cloud_height[i]][k +
                                                         self.cloud_pos[i]] = GRID_CONFIG['CODE']['CLOUD']

    def createGrass(self):
        max_x = PLAYER_CONFIG['SIZE']
        x_pos = max_x
        count = 0
        flag = True

        while count < self.numGrass:
            flag = True
            if count == 0:
                x_pos = randint(max_x + 3, max_x + 30)
            else:
                x_pos = randint(max_x + 10, max_x + 40)
            for i in range(0, 10, 1):
                if self._grid[self.actual_height - 1][x_pos + i] == GRID_CONFIG['CODE']['BLANK']:
                    flag = False
                    break
            if flag is True:
                count += 1
                max_x = x_pos
                self.grass_pos.append(x_pos)
            else:
                continue
        self.applyGrass()

    def applyGrass(self):
        for count in range(self.numGrass):
            for j in range(self.height - 1, self.height - 3, -1):
                for k in range(0, 3, 1):
                    if self._grid[j][k + self.grass_pos[count-1]] == GRID_CONFIG['CODE']['BLANK']:
                        self._grid[j][k + self.grass_pos[count-1]
                                      ] = GRID_CONFIG['CODE']['GRASS']

    def shift_window(self, player=None):
        if (self.width + self.window_left + (1 * player.speed)) < self.actual_width:
            self.window_left += (1 * player.speed)
            self.window_right += (1 * player.speed)
