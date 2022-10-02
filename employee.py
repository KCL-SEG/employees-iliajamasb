"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salaryPay, hoursWorked = 0, commissionAmount = 0, numberOfCommissions = 1):
        self.name = name
        self.salaryPay = salaryPay
        self.hoursWorked = hoursWorked
        self.commissionAmount = commissionAmount
        self.numberOfCommissions = numberOfCommissions

    def get_pay(self):
        
        pay = 0
        if self.hoursWorked != 0:
            pay += self.hoursWorked * self.salaryPay
        else:
            pay += self.salaryPay

        if self.commissionAmount != 0:
            pay += self.commissionAmount * self.numberOfCommissions

        return pay

    def __str__(self):
        returnText = ""
        returnText += self.name
        returnText += " works on a"
        if(self.hoursWorked == 1):
            returnText += " monthly salary of "+str(self.salaryPay) + ""
        else:
            returnText += " contract of " + str(self.hoursWorked) + " hours at " + str(self.salaryPay) + "/hour"

        if self.numberOfCommissions==0:
            returnText += ". "
        else:
            returnText += " and receives a"
            if self.numberOfCommissions > 1:
                returnText += " commission for " + str(self.numberOfCommissions) + " contract(s) at " + str(self.commissionAmount) + "/contract. "
            else:
                returnText += " bonus commission of " + str(self.commissionAmount) + ". "


        returnText += " Their total pay is " + str(self.get_pay()) + "."
                
        
        return returnText


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 1, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 1,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 1, 1500, 1,)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600, 1)

print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))

