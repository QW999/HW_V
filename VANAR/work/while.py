
# while True:
#     #print("BOO YA!")
#     answer = input("Do you wan't me to stop? ")
#     if answer != 'yes':
#         print("Try next")
#     else:
#         print('Executed')
#         break




n = 1
start_n = int(input())
end_n = int(input())

while n <= 10:
    if start_n < end_n:
        print(n)
        n += 1
    else:
        print(n)
        n = 10 - n
        break





# start = 1    # a) startimg conditions
# finish = 10  # b) finish conditions
#
# step = start
# while step <= finish:  # b) finish conditions
#     # code to repeat BEGIN
#     print(step)
#     # code to repeat END
#     step = step + 1   #c) how it iterates /  steps



start = 10
finish = 1
step = start
while step <= start and step >= finish:
    print(step)
    step = step - 1
print('END')

start = 10
finish = 1
while finish <= start:
    print(start)
    start = start - 1
print('END')

# n = 10
# while (n > 0):
#     print(n)
#     n = n - 1
# print("Done")