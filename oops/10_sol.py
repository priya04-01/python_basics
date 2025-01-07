# Multiple Inheritance
# Create two classes Battery andEngine, and let the ElectricCar class inherit from both
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_car+=1
  
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    @property
    def model(self):
        return self.__model
    @staticmethod
    def desc():
        return "Cars are amazing tools of transport"
        
class Battery:
    def battery_info(self):
        return "it is Battery operated"
class Engine:
    def engine_info(self):
        return "it has a powerful engine"

class ElectricCar(Car,Battery,Engine):
   pass

Car1=ElectricCar("Tesla","Model S")
Car2=Car("TATA","Safari",)
Car3=ElectricCar("Tesla","new")
print(Car3.full_name())
print(Car3.battery_info())
print(Car3.engine_info())

