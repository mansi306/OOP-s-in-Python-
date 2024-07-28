# operator overloading in python 
# int using + operator
num1 = 10
num2 = 20
print(num1+num2) # normal way
print(int.__add__(num1,num2)) # using special add method
print(num1.__add__(num2))
print(dir(int))
# string using + operator
n1 = "Raj"
n2 = "verma"
print(n1+n2) # normal way
print(str.__add__(n1,n2)) # using special add method
print(n1.__add__(n2))
print(dir(str))
# float using + operator
nm1 = float(input("enter a 1st number : "))
nm2 = float(input("enter a 2nd number : "))
print(nm1+nm2) # normal way
print(float.__add__(nm1,nm2)) # using special add method
print(nm1.__add__(nm2))
print(dir(float))
