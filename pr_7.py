# creation of static method 
class Bank:
    bank_name = "IDBI"
    rate_of_interest = 12.25
    @staticmethod
    def simple_interest(pr,n):
        interest = (pr*n*Bank.rate_of_interest)/100
        print("The rate of principal  interest is : ",interest)
pr = float(input("Enter the principal_interest ="))
n = int(input("Enter a number of year = "))
Bank.simple_interest(pr,n)