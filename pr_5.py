class Employee:
    company_name =input("Enter here your company name :")
    def __init__(self,name,sl):
        self.name =name
        self.salary = sl
    # create class method using decorator @classmethod
    @classmethod
    def get_company_name(cls):
        print(f"The company name is: ",cls.company_name)
e1 = Employee("raj",50000)
e2 = Employee("Mansi",10000000)
Employee.get_company_name()
