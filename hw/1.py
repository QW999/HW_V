
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





class Point:

    def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # print(str(self.x))
        # print(str(self.y))
        # print(str(other.x))
        # print(str(other.y))
        return Point(x, y)

p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1-p2
print(result.x, result.y) # prints (4,6)
