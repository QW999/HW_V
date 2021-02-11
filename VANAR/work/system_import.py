
from os import system


cinema = [0,1,2,1,0,0,0]


menu = "  Menu\n0. Exit\n1. Show the map\n2. Book ticket\n3. Confirm booking" \
       ""
option = -1


while option != 0:


    for i in cinema:
        if i == 0:
            print("[ ]", end=" ")
        elif i == 1:
            print("[R]", end=" ")
        elif i == 2:
            print("[X]", end=" ")

    print()
    system("cls") #clear
    print(menu)
    option = int(input("your choise> "))


    if option < 0 or option > 3:
        print('Pls enter correct choise!')

    if option == 0:
        print("Byeee!")


    elif option == 1:
        print("\nCINEMA MAP")
        for n in range(1, len(cinema) + 1, 1):
        # range incepe de la 1 pana la lungimea cinema cu pasul 1
            print("", n, end="  ")
        print()

        free_seats = 0
        for seat in cinema:
            if seat == 0:
                print("[ ]", end=" ")
                free_seats += 1
            elif seat == 1:
                print("[R]", end=" ")
            elif seat == 2:
                print("[X]", end=" ")

        print()
        print("free seats:", free_seats)
        input("\nHIT ENTER")


    elif option == 2:
        seat = int(input("Which seat?"))
        if cinema[seat-1] == 1:
            print("Alredy booked!!!")
        elif cinema[seat-1] == 2:
            print("Alredy sold!!!")
        else:
            cinema[seat - 1] = 1


    elif option == 3:
        seat = int(input("Which seat for confirmation?"))
        if cinema[seat-1] == 1:
            cinema[seat - 1] = 2
            print("Booking confirmed!!!")

        elif cinema[seat-1] == 2:
            print("Alredy sold!!!")
        else:
            print('Pls enter alredy booked seat!')


        input("\nHIT ENTER")
        print()

