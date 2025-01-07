# Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electric charge"

ElectricCar("Tesla","Model S","85kwh")
Car("TATA","Safari",)
Car("test","test")
print(Car.total_car)