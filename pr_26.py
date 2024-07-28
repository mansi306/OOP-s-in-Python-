# Need of property Decorator
class Employee:
    def __init__(self,first,last):# constructor
        self.firstname= first # instance variable
        self.lastname = last # instance variable
    @property # Property decorator
    def mail(self):
        return f"{self.firstname}{self.lastname}@gmail.com"
    @property # property decorator
    def fullname(self):# getter method
        return f"{self.firstname}{self.lastname}"
    @fullname.setter
    def fullname(self,name):# setter method
        first,last = name.split()
        self.firstname=first
        self.lastname=last        
e1 = Employee("Raj","verma")
e2 = Employee("Shivam","Patil")
e3 = Employee("Dnyanu","Deshmukh")
print(e1.mail)
e1.firstname="mansi"
print(e1.mail)
print(e1.fullname)
e2.fullname="Raj kapoor"
print("After setting :")
print(e2.fullname)