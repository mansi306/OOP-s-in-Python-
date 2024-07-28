# Encapsulation 
class Finanace:
    def __init__(self):
        self.revenue = 10000 # public member
        self.__Net_worth= 1000000 # private member (used __ before name )
        self.number_of_sales= 112
f1 = Finanace()
print(f1.__dict__)
class HR:
    def __init__(self):
        self.number_of_employee = 23
        print(f1.revenue)
        #print(f1.__Net_worth)
h1 = HR()
print(f1.__dict__)