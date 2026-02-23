#Multiple inheritance in python >

from Classes import Car


class Battery:
    def has_battery(self):
        return "this is Battery"
    
class Model:
    def has_model(self):
        return "This is Model"
    
class ElectricCar(Model , Battery, Car):
    pass

new_car =ElectricCar("TEsla" , "toyayo")
print(new_car.has_battery())        