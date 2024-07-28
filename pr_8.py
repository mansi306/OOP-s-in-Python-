# Inheritance
class Employee: # parent class
    bonus= 5000
    def display(self):
        print("This is a Employee class method")
# child class is inherited by parent class but it is not in viceversa
class Manager(Employee):# child class 
    bonus1 = 10000
    def show(self):
        print("This is a Manager class method")
e1 = Employee()
m1 = Manager()
print(m1.bonus)
e1.display()
m1.show()
m1.display()