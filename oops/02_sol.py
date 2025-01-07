# add a method to the car class that display the full name of the car(brand and model)

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_Car=Car("toyota","corolla")
print(my_Car.brand)
print(my_Car.model)
print(my_Car.full_name())