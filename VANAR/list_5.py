
from os import system


option = ''
over = False
robo_x = 5 # index 4
gmap = ['D','','','','x','♖','M','','','']  # 10values / index 9

while option != 'x':

    ########## print the map #############
    system("cls")
    print()
    print("-" * 20)
    for i in range(len(gmap)):
        print(gmap[i], end=' ')
    print()
    print("-" * 20)
    for i in range(len(gmap)):
        print(i, end=' ')
    print('\n\nCONTROLS: a - left, d - right, x - exit')
    ########## print the map #############


    ########## controls #############

    if over:
        print('GAME OVER')
        break
    option = input('>> ')
    if option == 'a':
        # print('left')
        gmap[robo_x] = ' '  # remove thr current position
        robo_x -= 1
        if gmap[robo_x] == 'D':  # Dinamit
            gmap[robo_x] = 'M'  # Mort
            over = True
        else:
            gmap[robo_x] = 'x'

    elif option == 'd':
        # print('right')
        gmap[robo_x] = ' '  # remove thr current position
        robo_x += 1
        # gmap[robo_x] = 'x'
        if gmap[robo_x] == 'D':  # Dinamit
            gmap[robo_x] = 'M'  # Mort
        else:
            gmap[robo_x] = 'x'

    elif option == 'x':
        print('GAME OVER')
    ########## controls #############




#   moove right/left   if 9 can not move right, limits
#   add var hp(healph points) = 100 each time Danger = -10....-100 = GAME OVER

