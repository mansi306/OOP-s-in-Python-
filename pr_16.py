# polymorphism with inheritance
class Vehicle:
    def __init__(self,name,color,price):# constructor
        self.name = name
        self.color = color
        self.price = price
    def get_details(self):# method 
        print("The name of the vehicle is : ",self.name)
        print(" The color of the vehicle is :",self.color)
        print("The Price of the vehicle is :",self.price)
    def max_speed(self):# method
        print("Maximum speed of the vehicle is 100m")
    def gear(self):
        print("Vehicle having 6 gears")
class Car(Vehicle):
    def max_speed(self):# method
        print("Maximum speed of the vehicle is 200m")
    def gear(self):
        print("Car having 7 gears")
v1 = Vehicle('BMW',"maroon",20000000)
c1 = Car("Lamborgini","Black",1000000000)
v1.get_details()
c1.get_details()
v1.max_speed()
c1.max_speed()
v1.gear()
c1.gear()

