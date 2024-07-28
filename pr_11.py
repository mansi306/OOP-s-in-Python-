# Heirarchical inheritance 
class Person:# parent class
    def __init__(self,name,age):# constructor
        self.name = name 
        self.age = age 
    def display(self):
        print("This is a person display method")
class Employee(Person):# child class
    def __init__(self,name,age,salary):
        super().__init__(name,age) # super class
        self.salary=salary
    def display1(self):
        print("This is a Employee display method")
class Student(Person):# child class
    def __init__(self,name,age,mark):
        super().__init__(name,age)# super class
        self.mark= mark
    def display2(self):
        print("This is a Student display method")
s1 = Student('raj',21,50)
p1= Person('ram',33)
e1 = Employee('mansi',22,100)
s1.display()
print(s1.__dict__)
print(p1.__dict__)
print(e1.__dict__)
p1.display() 
