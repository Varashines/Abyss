class Car:
    numberOfWheels = 4
    _color = "Black" ## Can be used outside class but not suggested
    __year = 2024 ## Can't be used outside class directly

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ",self._color)
        try:
            print("Year of manufacture: ",self.__year) # Shows error
        except:
            print("Couldn't access Private attribute")

car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
bmw = Bmw()
print("Private attribute yearOfManufacture: ", car._Car__year)
