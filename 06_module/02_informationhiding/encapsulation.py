class User :
    def __init__(self,username = None, password  = None):
        self.__username = username
        self.__password  = password
    
    def login(self,username, password):
        if ((self.__username.lower() == username.lower())
              and self.__password):
            print(
                "Access Granted against username:",
                self.__username.lower(),
                "and password:",
                self.__password)
        else : 
            print("granted")
    
    def setUsername(self,x):
        self.__username = x

    def getUserName(self):
        return(self.__username)
    
Steve = User("Steve", "12345")
Steve.login("steve", "12345") 
