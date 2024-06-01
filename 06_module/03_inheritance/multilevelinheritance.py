class Vehicle:
    def setTopSpeed(self , speed):
        self.topspeed = speed
        print("TopSpeed",self.topspeed)

class Car(Vehicle):
    def openTrunk(self):
        print("Trunk is open")


class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid")

priusPrime = Hybrid()
priusPrime.setTopSpeed(220)
priusPrime.openTrunk()
priusPrime.turnOnHybrid()