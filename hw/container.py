
class WindData:

    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction
        self.units = "m/s"

        print(type(speed))

    def __str__(self):
        return "Wind: " + str(self.speed) + self.units + "," + self.direction

    def __len__(self):
        return self.speed


    
wind_sunday = WindData(115, "SE")
wind_monday = WindData(95, "NW")

print(wind_sunday)
print(wind_monday)

print(len(wind_sunday))
print(len(wind_monday))
