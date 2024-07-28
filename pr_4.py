# class variables and class methods
class Employee:
    company_name = "Nvidia" # class variable
    def __init__(self,sal,age):
        self.salary = sal # instance variable
        self.age = age # instance variable
    def display(self):
        print(f"The salary is {self.salary}and age is {self.age}")
em1 = Employee(500000,23)
em2 = Employee(1000000,22)
print(Employee.company_name)
print(em1.company_name)
print(em2.company_name)
Employee.company_name="capgemini"
print(Employee.company_name)
em2.company_name="cognizant"
print(em2.__dict__)