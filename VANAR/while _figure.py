
# n = 1
# while n <=10:
#     print("*", end=" ")
#     n = n + 1



# n = 1
# while n <=10:
#     if n % 2 == 0:
#         print("#", end=" ")
#     else:
#         print("*", end=" ")
#     n += 1



# n = 1
# while n <=25:
#     if n % 2 == 0:
#         print("#", end=" ")
#     else:
#         print("*", end=" ")
#     if n % 5 == 0:
#         print()
#     n += 1



# n = 1
# while n <= 64:
#     if n % 2 == 0:
#         print("#", end=" ")
#     else:
#         print("*", end=" ")
#     if n % 8 == 0:
#         print()
#     n += 1



y = 1
while y <= 10:
    x = 1
    while x <= 10:
        if y == 1 or y == 10:
            print("#", end=" ")
        elif x == 1 or x == 10:
            print("#", end=" ")
        else:
            # print("*", end=" ")
            print(" ", end=" ")

        x += 1
    print()
    y += 1



a = int(input("nr: "))
y = 1
while y <= 10:
    x = 1
    while x <= 10:
        if y == 1 or y == 10:
            print("#", end=" ")
        elif x == 1 or x == 10:
            print("#", end=" ")
        else:
            print(" ", end=" ")

        x += 1
    print()
    y += 1




# n = int(input('nr: '))
# i = 0
# while i < n:
#     if i == 0:
#         j = 0
#         while j < n:
#             print(j + 1, end="")
#             j += 1
#         print()
#     elif i == n - 1:
#         j = 0
#         while j < n:
#             print(n - j, end="")
#             j += 1
#     else:
#         print(i + 1, end="")
#         j = 0
#         while j < n - 2:
#             print(" ", end="")
#             j += 1
#         print(n - i)
#     i += 1


