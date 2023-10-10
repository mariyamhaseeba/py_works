class Bike:
    def start(self):
        print("kicker start")
    def breaking(self):
        print("drum break")
class HeroHondaSplender(Bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs breaking")
obj1=HeroHondaSplender()
obj1.start()
obj1.breaking()