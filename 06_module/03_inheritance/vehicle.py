class Vehicle:
   fuelCap = 50
   def display(self):
       print("I am from the vehicle class")

class Car(Vehicle):
    fuelCap = 100
    def display(self):
        super().display()
        print("Fuel Cap from Super",super().fuelCap)
        print("Fuel cap from child class",self.fuelCap)
obj1= Car()
obj1.display()


    