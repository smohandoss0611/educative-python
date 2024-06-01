class Student:
    def __init__(self, name = None, rolenumber = None):
        self.__name = name
        self.__rolenumber = rolenumber

    def setName(self,name):
        self.__name = name 
    
    def getName(self):
        return self.__name
    
    def setRoleNumber(self,rolenumber):
        self.__rolenumber = rolenumber
    
    def getRoleNumber(self):
        return self.__rolenumber
    


student = Student("Janesh",123)
print(student)
student.setName("Bhavesh")
print(student.getName())
student.setRoleNumber("234")
print(student.getRoleNumber())