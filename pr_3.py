# creating instance variable using instance method
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def display(self):
        print(self.name,self.mark)
    def change_data(self):
        self.name = input("enter new name = ")
        self.age =int(input("enter your = "))
std1=Student('akshay',23)
std2=Student('raj',34)
std3=Student('ram',32)
std1.display()
std2.display()
std3.display()
std1.change_data()
print(std1.__dict__)