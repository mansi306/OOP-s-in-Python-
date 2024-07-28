class Father:
    def __init__(self):
        print("Father constructor called")
        self.vehicle = "scooter"
class Son(Father):
    def __init__(self):
        print("son constructor called")
        self.vehicle="BMW"
    
s = Son()
print(s.__dict__)
