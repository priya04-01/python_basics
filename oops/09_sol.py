# Demonstrate the use of the isinstance() to check if my_tesla is an instance of Car and ElectricCar
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
        
class ElectricCar(Car):
    def __init__(self,__brand,__model, battery_size):
        super().__init__(__brand,__model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric charge"

Car1=ElectricCar("Tesla","Model S","85kwh")
my_tesla=ElectricCar("Tesla","Model R","79kwh")
Car2=Car("TATA","Safari",) 
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))