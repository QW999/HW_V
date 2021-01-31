
def drawLine( length, direction ):
    if direction == 'h':
        print('-' * length)
    if direction == 'v':
        print('\n|' * length)

drawLine( 5, 'h' )
drawLine( 3, 'v' )
