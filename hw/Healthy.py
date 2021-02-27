

class Healthy():
    def healthy(self):
        print("feeling healthy")

class Ill(Healthy):
    def ill(self):
        print("feeling ill")

class Curred(Healthy):
    def curred(self):
        print("feeling curred")


pacient = Healthy()

Healthy().healthy()

COVID_pozitiv = Ill()
COVID_negativ = Curred()

COVID_pozitiv.ill()
COVID_negativ.curred()
