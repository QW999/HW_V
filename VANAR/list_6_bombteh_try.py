
from os import system

robo_r = 0
robo_c = 0
option = ''
over = False


gmap = [
    ['X','B','H','H','H'],  # 0   ♘  ✠  ⚔
    ['H','H','H','B','H'],  # 1
    ['H','H','H','H','H'],  # 2
    ['H','H','B','H','H'],  # 3
    ['H','H','H','H','H']   # 4
]   # 0,  1,  2,  3,  4


while option != 'x':
    try:

        ########## print the map #############
        system("cls")
        print()
        print("-" * 10)
        for r in range(len(gmap)):
            for c in range(len(gmap)):
                print(gmap[r][c], end=' ')
            print('|')
        print("-" * 10)
        print('\n\nCONTROLS: \na - left, \nd - right, \nx - exit, \nw - streeght, \ns - down' )
        ########## print the map #############

        ########## controls #############
        if over:
            print()
            print('GAME OVER')
            break

          
        option = input('>> ')

        
        if option == 'a':
            gmap[robo_r][robo_c] = 'H'
            robo_c -= 1

        if option == 'd':
            gmap[robo_r][robo_c] = 'H'
            robo_c += 1

        if option == 'w':
            gmap[robo_r][robo_c] = 'H'
            robo_r -= 1

        if option == 's':
            gmap[robo_r][robo_c] = 'H'
            robo_r += 1

            
        if gmap[robo_r][robo_c] == 'B':
            over = True
            gmap[robo_r][robo_c] = 'D'
        else:
            gmap[robo_r][robo_c] = 'X'

            
        if option == 'x':
            print('GAME OVER')
        ########## controls #############

    except IndexError:
        print('list assignment index out of range')
        print('GAME OVER')
        break


# add movement left streeght
# add limits
# add mines + GAME OVER conditions
