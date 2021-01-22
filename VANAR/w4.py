gmap = [
    ['X','B','H','H','H'],  # 0   ♘  ✠  ⚔
    ['H','H','H','B','H'],  # 1
    ['H','H','H','H','H'],  # 2
    ['H','H','B','H','H'],  # 3
    ['H','H','H','H','H']   # 4
]   # 0,  1,  2,  3,  4

for r in range(len(gmap[0])):
    for c in range(len(gmap[0])):
        print(gmap[r][c], end=' ')
    print("*")



print(gmap)
# for r in range(len(gmap[0])):
#     for c in range(len(gmap[0])):
#         print(gmap[r][c], end=' ')
#     print("*")