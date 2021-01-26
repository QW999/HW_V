

# def Week_eval_temperature(Lu, Ma, Mi, Jo, Vi, Sa, Du):
def Week_eval_temperature():
    # Week_temperature = (Lu + Ma + Mi + Jo + Vi + Sa + Du) / 7
    # temp = int(input('Today temperature: '))
    Lu = int(input('Lu t: '))
    Ma =  int(input('Ma t: '))
    Mi =  int(input('Mi t: '))
    Jo =  int(input('Jo t: '))
    Vi =  int(input('Vi t: '))
    Sa =  int(input('Sa t: '))
    Du =  int(input('Du t: ')))

    temp = (Lu + Ma + Mi + Jo + Vi + Sa + Du) / 7

    # print('Week_eval_temperature: ', round(Week_temperature, 2))
    def eval_temperature(temp):
        if temp >= 50:
            print("Very hot")
        elif temp < 50 and temp >= 30:
            print("Hot")
        elif temp < 30 and temp >= 15:
            print("Warm")
        elif temp < 15 and temp >= 0:
            print("OK")
        elif temp < 0 and temp >= -10:
            print("Cold")
        else:
            print("Very Cold")

    # eval_temperature(int(input('Today temperature: ')))
    eval_temperature(temp)


Week_eval_temperature()