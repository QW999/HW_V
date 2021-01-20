
# from math import log, floor
#
# def human_format(number):
#
#     units = ['', 'K', 'M', 'G', 'T', 'P']
#     k = 1000.0
#     magnitude = int(floor(log(number, k)))
#     return '%.2f%s' % (number / k ** magnitude, units[magnitude])



def askint():
    while True:
        try:
            val = int(input("Input an integer: "))
    #        if val != int:
    #            print("null")
        except:
            print("An error occurred! Please try again!")
            continue
#        else:
 #           import math
  #          print("Thank you, your number squared is: {}".format(math.sqrt(val)))
        else:
            import math
            print("Thank you, your number squared is: {}".format(val ** 2))
            break
#        finally:
 #           print("Finally, I executed!")
askint()