# Top 21 magic Methods and Attributes in python
# 1) __init__(self):
# This method is called automatically to initialize instance attributes when an object is created 
class Bank :
    bank_name = "Welcome to the IDBI Bank !!"
    def __init__(self,balance,adhar_no,acc_no,name):
        print("init is running ")
        self.bank_balance = balance
        self.adhar_number =adhar_no
        self.account_number=acc_no
        self.customer_name = name
    def __str__(self):
        return "This is from str "
    def __repr__(self):
        return "This is from repr"

b1 = Bank(100000,"2345 4567 4455",244455554,"Ram chavan")
print("Bank balance is :",b1.bank_balance)
b1.bank_balance = b1.bank_balance + 1000
print("The current bank balance is ",b1.bank_balance)


# 2) __dict__ :
# It gives dictionary containing instance variables and their values if you call it with object
print(b1.__dict__)
print(Bank.__dict__) # __dict__ returns namespace of class/object

# 3) __new__():
# python implicitly calls the .__new__() method as a first step in the instantiation process 

# 4) __str__():
# In python __str__() method used to define a string representation of an object
print(b1) # b1.__str__()


# 4) __repr__(): str having the higher priority than repr()
# In python the __repr()__ method is a special method used to define a string representation of an object

# __len__()
# In python the len() method is a special method used to define the length of a object
print(len([10,20,49,4,56])) # list is an built in datatype 
