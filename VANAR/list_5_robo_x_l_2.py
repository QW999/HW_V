
from os import system


option = ''
over = False
robo_x = 5 # index 5
gmap = [' ',' ',' ',' ',' ','♖',' ',' ',' ',' ']  # 10values / index 9  ⚔

while option != 'x':

    ########## print the map #############
    system('cls')
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
    try:

        option = input('>> ')
        if option == 'a':
            # print('left')
            gmap[robo_x] = ' '  # remove thr current position
            robo_x -= 1
            if gmap[robo_x] == '⚔':  # Dinamit
                gmap[robo_x] = '☠'  # Mort
                over = True
            else:
                gmap[robo_x] = '♖'   # placeit on this position

        elif option == 'd':
            # print('right')
            gmap[robo_x] = ' '
            robo_x += 1
            if gmap[robo_x] == '⚔':  # Dinamit
                gmap[robo_x] = '☠'  # Mort
                over = True
            else:
                gmap[robo_x] = '♖'


        elif option == 'x':
            print('GAME OVER')
        ########## controls #############

    except IndexError:
        over = True
        print('list assignment index out of range')



#   moove right/left   if 9 can not move right, limits
#   add var hp(healph points) = 100 each time Danger = -10....-100 = GAME OVER

