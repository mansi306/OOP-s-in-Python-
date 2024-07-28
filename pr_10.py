# super function
class Computer(object):
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage= storage
        print("Computer constuctor is called")
class Mobile(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)
        self.model="iphone"
        print("mobile class constructor is called")
Apple =Mobile('8gb','512gb')
print(Apple.__dict__)

