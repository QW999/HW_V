

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

eval_temperature(int(input('Enter temperature: ')))



