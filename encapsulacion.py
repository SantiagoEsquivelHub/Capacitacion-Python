class Prueba :
    def __init__(self):
        self.__private = "Soy privado"
        self.private = "Soy publico"

    def __privateMethod(self): 
        print("You've use a private method")

    def publicMethod(self): 
        print("You've use a public method")

    def getPrivate(self):
        return self.__private   

    def setPrivate(self, value):
        self.__private = value

obj = Prueba()

# print(obj.__private)
# print(obj.__private)

obj.setPrivate("new value")
print(obj.getPrivate())
