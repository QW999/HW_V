a = int(input("Enter a value: "))
for row in range (0,a):
    for col in range (0,a):
        if(col==0 or col==(a-1) or ((row==0 or row==(a-1)) and (col>0 and col<(a-1)))):
            print("* ", end="")
        else:
            print("  ", end="")
    print()

a = 5
for row in range (-1,a + 1):
    for col in range (-1,a + 1):
        if(col==0 or col==(a-1) or ((row==0 or row==(a-1)) and (col>0 and col<(a-1)))):
            print("H", end="")
        else:
            print("*", end="")
    print()