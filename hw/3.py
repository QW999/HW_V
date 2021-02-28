import datetime
class Healthy:
    def __init__(self, fullName):
        self.ill = self.Ill()
        self.curred = self.ill.Curred()
        self.fullName = fullName
        self.today = datetime.date.today()
        print("Today date: ", self.today)
    def __str__(self):
        return "fullName: " + str(self.fullName)
    def healthy(self):
        return self.fullName + " is healthy"
    class Ill:
        def __init__(self):
            self.startDate = datetime.date(2021, 2, 1)
            self.endDate = datetime.date(2021, 2, 15)
            self.Quarantine = self.endDate - self.startDate
            self.curred = self.Curred()
        # def __str__(self):
        #     return str(self.curred) + str(self.startDate) + str(self.endDate)
        class Curred:
            def getPeriod(self):
                return "Quarantine: "


        def inner_display(self, msg):
            print("This is Ill class")
            print(msg)
pacient = Healthy("Igor Nicolaevici")
print(pacient)
print(pacient.healthy())

# ill = healthy.Ill()
getPeriod.getPeriod("sss")