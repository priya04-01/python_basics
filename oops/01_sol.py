# basic Class and object
# create a car  class with attributes like brand and model . then create an instance
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_Car=Car("toyota","corolla")
print(my_Car.brand)
print(my_Car.model)