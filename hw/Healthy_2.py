
class Healthy:
    def __init__(self, fullName):
        self.fullName = fullName
    def __str__(self):
        return "Patient: " + str(self.fullName)
    def healthy(self):
        print(self.fullName, "feeling healthy")

class Ill(Healthy):
    def ill(self, startDate):
        self.startDate = startDate
        print(self.fullName, "feeling ill")
    def __str__(self):
        return "self.startDate: " + str(self.startDate)

    # class Curred(Healthy):
    #     def curred(self, endDate):
    #         self.endDate = endDate
    #         print("self.endDate: ", end="  ")
    #         print(self.fullName, "feeling curred")
    #     def __str__(self):
    #         return str(self.endDate)





# pacient = Healthy(int(input()))
pacient = Healthy("Chiu")
print(pacient)

# Healthy("Chiu").healthy()
print(pacient.healthy())



COVID_positive = Ill({"day": 10, "month": 2, "year": 2021})
# COVID_negative.curred({"day": 24, "month": 2, "year": 2021})

print(COVID_positive.ill("Chiu"))