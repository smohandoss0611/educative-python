class CombustionEngine():
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = 34

class ElectricEngine():
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine,ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:",self.tankCapacity)
        print("Charging Capacity",self.chargeCapacity)


car = HybridEngine()
car.setTankCapacity(33)
car.setChargeCapacity(34)
car.printDetails()