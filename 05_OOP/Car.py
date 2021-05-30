class Car():

    def __init__(self):
        self.__chasisLenght = 250
        self.__chasisWidth = 120
        self.__wheels = 4
        self.color = "red"
        self.__start = False

    def run(self, run):
        self.start = run
        if(self.start):
            self.internal_check

    def status(self):
        if (self.start):
            return "Car is running"
        else:
            return "Car is stopped"

    def internal_check(self):
        print("Internal check")
        self.gasoline = "Ok"
        self.oil = "Ok"

        if(self.oil == "Ok" and self.oil == "Ok"):
            return True
        else:
            return False

###################################################
myCar = Car()
print(myCar.color)
myCar.run(True)
print(myCar.color)
print(myCar.status())
