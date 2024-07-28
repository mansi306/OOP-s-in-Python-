# Abstraction in python 
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    def Color(self):
        print("Color of the car is White")

class Maruti_suzuki(Car):
    def mileage(self):
        print("Mileage is 25Kmph")

class Bugatti(Car):
    def mileage(self):
        print("Mileage is 30Kmph")

class Safari(Car):
    def mileage(self):
        print("Mileage is 50Kmph")

# Instantiate the subclasses
m1 = Maruti_suzuki()
b1 = Bugatti()
s1 = Safari()

# Call methods on the instances
m1.mileage()
b1.mileage()
s1.mileage()
m1.Color()
b1.Color()
s1.Color()
