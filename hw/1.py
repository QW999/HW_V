
class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    # def __str__(self):   # costumer
    #     return str(self.mileage)

    # def __repr__(self):   # developer
    #     return repr(self.mileage)
    def __repr__(self):   # developer
        return "The object " + repr(self.name) + " has " + repr(self.mileage) + " mileage"

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"


Honda = Car("Honda City", 21.4)
# print(Honda.max_speed(150))

Skoda = Car("Skoda Octavia", 13)
# print(Skoda.max_speed(210))

print(Honda)
print(Skoda)

