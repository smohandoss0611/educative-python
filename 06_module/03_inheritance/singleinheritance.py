class Vehicle:
    def setTopSpeed(self, speed):
        self.topspeed = speed
        print("Top speed is set to",self.topspeed)

class Car(Vehicle):
    def openTrunk(self):
        print('Trunk is now  open()')


corolla = Car()
corolla.setTopSpeed(20)
corolla.openTrunk()