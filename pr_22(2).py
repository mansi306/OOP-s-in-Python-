class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name = name 
        self.roll= roll
        self.dob = self.DOB(dd,mm,yy)
    def display(self):
        print(f"Name of the student is :{self.name} and Roll number is: {self.roll}")
        self.dob.display()
    
    class DOB:
        def __init__(self,dd,mm,yy):
            self.date = dd
            self.month= mm
            self.year = yy
        def display(self):
            print(f"Date of Birth is :{self.date}/{self.month}/{self.year}")
s1 = Student("Raj",1,24,6,2003)
s1.display()