class Engine:
    def setPower(self, power):
        self.power = power

class CombustionEngine(Engine):
    def setTankCapacity(self , tankcapacity):
        self.tankcapacity = tankcapacity


class ElectricEngine(Engine):
    def setChargingCapacity(self , chargingCapacity):
        self.chargingCapacity = chargingCapacity


class HybridEngine(CombustionEngine,ElectricEngine):
    def printDetails(self):
        print("power",self.power)
        print("chargingcapacity",self.chargingCapacity)
        print("tankcapacity",self.tankcapacity)

car = HybridEngine()
car.setPower("4343 CC")
car.setTankCapacity("434343")
car.setChargingCapacity("434343")
car.printDetails()