class Country:# parent class
    def __init__(self): # Country class constructor
        print("this is country class ")
        self.office = "delhi"
class State :# parent class
    def __init__(self): # state class constructor
        super().__init__()
        print("this is stete class")
        self.office="mumbai"
class District(State,Country):# child class
    def __init__(self): # district class constructor
        super().__init__()
        print("This is District class constuctor")
        self.office="pune"
d1 = District()
print(d1.__dict__)