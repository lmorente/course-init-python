class Vehicle():
    def __init__(self, brand, modele):
        self.brand = brand
        self.modele = modele
        self.start = False
        self.acceleration = False
        self.braking = False

    def run(self):
        self.start = True

    def accelerate(self):
        self.acceleration  = True

    def brake(self):
        self.braking = True

    def status(self):
        print("Brand: ", self.brand, "\nModele: ", self.modele, "\nStart: ", self.start,
              "\nAcceleration:", self.acceleration, "\nBraking:", self.braking)

class Electric_vehicle():
    load = 0
    def recharge(self):
        self.load = 100

class Motorcycle(Vehicle):
    two_wheels = True

    def go_two_wheels(self):
        print("Go two wheels")

    def status(self):
        print("Brand: ", self.brand, "\nModele: ", self.modele, "\nStart: ", self.start,
              "\nAcceleration:", self.acceleration, "\nBraking:", self.braking,"\nTwo wheels:", self.two_wheels)

miMotorcycle = Motorcycle("Honda", "CBR")
miMotorcycle.status()
miMotorcycle.go_two_wheels()

class Electricbike(Electric_vehicle, Vehicle):
    pass