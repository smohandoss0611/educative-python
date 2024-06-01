class Vehicle:
    def setTopsSpeed(self, speed):
        self.speed = speed
        print(self.speed)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

corolla = Car()
corolla.setTopsSpeed(344)

volvo = Truck()
volvo.setTopsSpeed(343)