# Static method is a method that belongs to the class rather than an instance of the class
# Add a static method to the car class that returns a general description of a car 
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    @staticmethod
    def desc():
        return "Cars are amazing tools of transport"
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
print(Car.desc())