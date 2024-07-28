# Inner class or Nested class:
class Outer:
    def __init__(self):
        print("The outer Constructor is called")
    def display(self):
        print("DIsplay method is called")# instance method
    class Inner: # nested class
        def __init__(self):
            print("Inner constructor is called")
        def show(self):
            print("Show method is called")# instance method
obj = Outer()
i1 = obj.Inner()
i1.show()
obj.display()