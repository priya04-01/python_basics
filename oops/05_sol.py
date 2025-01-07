# Polymorphism
# Polymorphism is the ability of an object to take on multiple forms. This can be achieved through method overriding or method overloading.
# demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,but different behaviors
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
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

my_Car=ElectricCar("Tesla","Model S","85kwh")
safari=Car("TATA","Safari",)
print(my_Car.full_name())
print(my_Car.fuel_type())
print(safari.full_name())
print(safari.fuel_type())
