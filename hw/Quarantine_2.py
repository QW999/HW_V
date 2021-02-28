import datetime
class Healthy:
    def __init__(self, Name):
        self.ill = self.Ill()
        self.curred = self.ill.Curred()
        self.Name = Name
    def __str__(self):
        return "Name: " + str(self.Name)
    def healthy(self):
        return self.Name + " is healthy"
    class Ill:
        def __init__(self):
            self.curred = self.Curred()
            self.today = datetime.date.today()
            self.startDate = datetime.date(2021, 2, 1)
            self.Days_after_infect = self.today - self.startDate
        def __str__(self):
             return "Infection date: " + str(self.startDate) + " / " + str(self.curred) + " / Days_after_infect" + str(self.Days_after_infect)
        class Curred:
            def __init__(self):
                self.startDate = datetime.date(2021, 2, 1)
                self.endDate = datetime.date(2021, 2, 15)
                self.Quarantine = self.endDate - self.startDate
            def __str__(self):
                return "Quarantine period: " + str(self.Quarantine)

pacient = Healthy("Igor Nicolaevici")
print(pacient)
print(pacient.healthy())
ill = Healthy.Ill()
print(ill)
curred = Healthy.Ill.Curred()
print(curred)
