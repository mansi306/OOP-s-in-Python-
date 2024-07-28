# callable in python (__call__) magic method:
# classes and functions are always callable in python 
class Add(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __call__(self,a,b): # magic method
        return a+b
add = Add(10,20)
print(callable(Add)) # True ( because classes are callable as function)
print(add(10,30))
print(callable(add)) # false ( because objects are not callable)/ (True because using call magic method it becomes callable .)
