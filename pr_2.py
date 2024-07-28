class Student:
    def __init__(self,name,mark):# self contains memory location of the current object
        self.name = name 
        self.marks= mark
std_1 = Student('mansi',100)
std_2 = Student('neha',99)
std_3 = Student('Akash',98)
print(std_1.name)
std_1.name ='Manu'
print(std_1.name)
# creating instance variable outside the class
std_2.age=21
print(std_2.__dict__)
del std_2.name
print(std_2.__dict__)