def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f"There are {num} of {belt} belts")

def ninja_itro(dictionary):
    for key, val in dictionary.items():
        print(f"I am {key} and I am {val} belt")
ninja_belts = {}
while True:
    ninja_name = input("Enter name: ")
    ninja_belt = input("Enter belt colour: ")
    ninja_belts[ninja_name] = ninja_belt
    another = input("Ad another member? (y/n)")
    #adaugam urmatorul el y-yes/n-no (finalizam operatiunea)
    if another == "y":
        continue
    else:
        break
ninja_itro(ninja_belts)