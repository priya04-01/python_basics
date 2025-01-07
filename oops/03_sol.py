# Inheritance
# Create an electricCar class that inherits from the Car class and has an additional attribute battery_size

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size


my_Car=ElectricCar("Tesla","Model S","85kwh")

print(my_Car.full_name())
print(my_Car.battery_size)
