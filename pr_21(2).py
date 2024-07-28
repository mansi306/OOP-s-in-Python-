# method overloading in pthon (example-2)
class Area:
    def area(self,l=None,b=None):
        if l!=None and b!=None:
            print("The Area is :",l*b)
        elif l!=None:
            print("The Area is :",l*l)
        else:
            print("Incorrect parameters is passed")
a = Area()
a.area(10,20)
a.area(10)