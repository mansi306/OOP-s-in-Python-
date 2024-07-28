# Polymorphism in functions and objects
class Ferrari:
    def fuel_type(self):
        print("Petrol")
    def Max_speed(self):
        print("maximum speed of ferrari is:")
class BMW:
    def fuel_type(self):
        print("Diesel")
    def Max_speed(self):
        print("maximum speed of BMW is:")
def car_details(obj):
    obj.fuel_type()
    obj.Max_speed()
ferrari=Ferrari()
bmw=BMW()
car_details(bmw)
print("details of bmw")
car_details(ferrari)
print("details of ferrari")
