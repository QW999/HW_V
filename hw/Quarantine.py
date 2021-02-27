import datetime


class Feeling:

    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.sd2 = datetime.date(2021, 2, 1)
        self.ed2 = datetime.date(2021, 2, 15)
        self.today = datetime.date.today()

    def __str__(self):
        return str(self.name) + " feeling excited"


class Healthy(Feeling):

    def __repr__(self):
        return repr(self.name)

    def healthy(self):
        return self.name + " feeling healthy"


class Ill(Feeling):
    def ill(self):
        print("Today date:", self.today)
        Days_after_i = self.today - self.sd2
        return self.name + " feeling ill  " + str(self.startDate) + \
               "\nDays after infection: " + str(Days_after_i)


class Curred(Ill):
    def curred(self):
        return self.name + " curred at " + str(self.endDate)

    def getPeriod(self):
        Quarantine = self.ed2 - self.sd2
        return "Quarantine period: " + str(Quarantine)


sd = {"day": 1, "month": 2, "year": 2021}
ed = {"day": 15, "month": 2, "year": 2021}

pacient_1 = Feeling("Mars", sd, ed)
print(pacient_1)

pacient_2 = Healthy("Apollo", sd, ed)
print(pacient_2.healthy())

pacient_3 = Ill("Jupiter", sd, ed)
print(pacient_3.ill())

pacient_4 = Curred("Venus", sd, ed)
print(pacient_4.curred())
print(pacient_4.getPeriod())










