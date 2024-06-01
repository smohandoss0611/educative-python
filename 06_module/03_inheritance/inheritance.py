class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print ("Manufacturer",self.make)
        print("color",self.color)
        print("model",self.model)


class Car(Vehicle):
    def __init__(self, make, color, model,doors):
         super().__init__(make, color, model)
         self.doors = doors
    
    def printCarDetails(self):
        self.printDetails()
        print("Doors:" ,self.doors)


class ParentClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
class ChildClass(ParentClass):
    def __init__(self , a , b , c):
        super().__init__(a, b , c)
        self.c = c

obj = ChildClass()
print(obj.a)
print(obj.b)
print(obj.c)

    
    
c  = Car("Tesla","Red","Model S",1)
c.printCarDetails()
    
    
     