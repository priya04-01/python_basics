# Encapsulation
# encapsulation is a mechanism of hiding the internal state of an object from the outside world.
# modify the car class to encapsulate the brand attribute , make it private and provide a getter method for it.
class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    def get_brand(self):    
        return self.__brand +"!!"
    def get_model(self):
        return self.__model+"!"
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    

    
my_Car=Car("Tesla","Model S")

print(my_Car.get_brand())
print(my_Car.full_name())