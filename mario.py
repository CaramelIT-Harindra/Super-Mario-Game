from colorama import Back, init

init(autoreset=True, convert=None, strip=None, wrap=True)

mario = [
    [0, 3, 3, 3, 3, ],
    [0, 1, 4, 1, 0, ],
    [0, 1, 1, 1, 1, ],
    [0, 1, 1, 1, 0, ],
    [3, 2, 3, 2, 3, ],
    [1, 3, 3, 3, 1, ],
    [0, 3, 3, 3, 0, ],
    [0, 2, 0, 2, 0, ],
]

for i in range(8):
    for j in range(5):
        if mario[i][j] == 0:
            print(' ', end='')
        elif mario[i][j] == 1:
            print(Back.YELLOW + ' ', end='')
        elif mario[i][j] == 2:
            print(Back.BLUE + ' ', end='')
        elif mario[i][j] == 3:
            print(Back.RED + ' ', end='')
        elif mario[i][j] == 4:
            print(Back.BLACK + ' ', end='')

    print(" ")
