from config import GRID_CONFIG
from colorama import Fore, Back, Style, init

# init(autoreset=True)


class Scene:
    '''Characteristics of game screen'''

    def __init__(self):
        '''Contructor for game screen'''
        self.height = GRID_CONFIG['HEIGHT']
        self.width = GRID_CONFIG['WIDTH']
        self._grid = [[GRID_CONFIG['CODE']['BLANK']]
                      * self.width for n in range(self.height)]

    # def render(self, player=None, enemies=None):
    #     for row in range(self.height):
    #         for col in range(self.width):
    #             if self._grid[row][col] == GRID_CONFIG['CODE']['BLANK']:
    #                 print(Back.GREEN + " ", end='')
    #             elif self._grid[row][col] == GRID_CONFIG['CODE']['PLAYER']:
    #                 pass
    #                 # Print PLAYER
    #             elif self._grid[row][col] == GRID_CONFIG['CODE']['ENEMY']:
    #                 pass
    #                 # Print ENEMY
    #             elif self._grid[row][col] == GRID_CONFIG['CODE']['OBSTACLE']:
    #                 pass
    #                 # Print Obstacle
    #             else:
    #                 self._grid[row][col] = 0
    #                 print(Back.GREEN + " ", end='')
    #         print(Back.RESET + '')
    def render(self, player=None, enemies=None):
        if player is None:
            return
        else:
            self._grid[self.height-3][4] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-3][5] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-3][6] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-3][7] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-3][8] = GRID_CONFIG['CODE']['OBSTACLE']

            self._grid[self.height-5][12] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-5][13] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-5][14] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-5][15] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-5][16] = GRID_CONFIG['CODE']['OBSTACLE']

            self._grid[self.height-7][20] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-7][21] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-7][22] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-7][23] = GRID_CONFIG['CODE']['OBSTACLE']
            self._grid[self.height-7][24] = GRID_CONFIG['CODE']['OBSTACLE']

            self._grid[player.pos['y']][player.pos['x']
                                        ] = GRID_CONFIG['CODE']['PLAYER']
            for row in range(self.height):
                for col in range(self.width):
                    if self._grid[row][col] == GRID_CONFIG['CODE']['BLANK']:
                        print(Back.GREEN + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['PLAYER']:
                        print(Back.RED + " ", end='')
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['ENEMY']:
                        pass
                        # Print ENEMY
                    elif self._grid[row][col] == GRID_CONFIG['CODE']['OBSTACLE']:
                        print(Back.LIGHTBLACK_EX + " ", end='')
                    else:
                        self._grid[row][col] = 0
                        print(Back.GREEN + " ", end='')
                print(Back.RESET + '')
