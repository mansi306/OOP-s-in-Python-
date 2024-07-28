# Method overloading in python(example-1)
class Addition:
    def add (self,num1=None,num2=None,num3=None):
        if num1!=None and num2!=None and num3!=None:
            print("Addition is :",num1+num2+num3)
        elif num1!=None and num2!=None:
            print("Addition is :",num1+num2)
        else:
            print("Incorrect parameter is passed.")
   
a = Addition()
a.add(10,20)
a.add(10,90,78)