class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def electric_info(self):
        print("This is an electric car")

obj = ElectricCar()
obj.vehicle_info()
obj.car_info()
obj.electric_info()