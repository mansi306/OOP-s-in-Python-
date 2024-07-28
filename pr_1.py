class Demo:
    pass
d1=Demo()
class Employee:
    '''This is a employee class for maintaning employee data '''
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def display(self):
        print(f"name is {self.name} and the age is {self.age}")
e1 = Employee ('mansi',22)
e2 = Employee ('neha',22)
print(Employee.__doc__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(isinstance(e1,Employee))
print(isinstance(d1,Employee))