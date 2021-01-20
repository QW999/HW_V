
from os import system

robo_r = 0
robo_c = 0

gmap = [
    ['X',' ',' ',' ',' '],  # 0
    [' ',' ',' ',' ',' '],  # 1
    [' ',' ',' ',' ',' '],  # 2
    [' ',' ',' ',' ',' '],  # 3
    [' ',' ',' ',' ',' '],  # 4
]   # 0,  1,  2,  3,  4

# print(gmap[0][4])


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
option = input('>> ')
if option == 'd':
    gmap[robo_r][robo_c] = ' '
    robo_c += 1
    gmap[robo_r][robo_c] = 'X'

if option == 's':
    gmap[robo_r][robo_c] = ' '
    robo_r += 1
    gmap[robo_r][robo_c] = 'X'
########## controls #############



# add movement left streeght
# add limits
# add mines + GAME OVER conditions