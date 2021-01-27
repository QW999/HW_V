def Week_eval_temperature():
    Lu = int(input('Lu t: '))
    Ma =  int(input('Ma t: '))
    Mi =  int(input('Mi t: '))
    Jo =  int(input('Jo t: '))
    Vi =  int(input('Vi t: '))
    Sa =  int(input('Sa t: '))
    Du =  int(input('Du t: '))

    temp = (Lu + Ma + Mi + Jo + Vi + Sa + Du) / 7
    print('Week_eval_temperature: ', round(temp, 2), '°C')

    ct = input('Enter city: ')


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
    print('eval_temperature: ')
    eval_temperature(temp)
    et = eval_temperature(temp)


    def city(ct):
        RM = ['Anenii Noi','Basarabeasca','Briceni','Cahul','Cantemir','Călărași','Căușeni','Cimișlia',
              'Criuleni','Dondușeni','Drochia','Dubăsari','Edineț','Fălești','Florești','Glodeni',
              'Hîncești','Ialoveni','Leova','Nisporeni','Ocnița','Orhei','Rezina','Rîșcani','Sîngerei',
              'Soroca','Strășeni','Șoldănești','Ștefan Vodă','Taraclia','Telenești','Ungheni']
        if ct in RM:
            print('In RM, ', ct, ' weather is', round(temp, 2), '°C'", 'is', eval_temperature(temp)")
        else:
            print('Over the border in ', ct, ' weather is', round(temp, 2), '°C'", 'is', eval_temperature(temp)")
    city(ct)



print('Week_eval_temperature')
Week_eval_temperature()