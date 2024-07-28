class Emoployee:
    def setName(self,name):# setter method
        self.name = name
    def getName(self): # getter method
        print(f"The name of the Employee is : {self.name}")
e1 = Emoployee()
e2 = Emoployee()
e1.setName(input("Enter your name :"))
e2.setName(input("Enter your name :"))
print("e1 object is :",e1.__dict__)
print("e2 object is :",e2.__dict__)
e1.getName()
e2.getName()
