#
'''
class Person:
     def __init__(self, name, age):
          self.name = name
          self.age = age

     def showName(self):
          print("Employee Name is = ",self.name)

     def showAge(self):
          print("Employee Age is = ",self.age)
     
class Employee(Person):
     def __init__(self, name, age, salary):
          super().__init__(name,age)
          self.salary = salary

     def showEmployeeData(self):
          super().showName()
          super().showAge()
          print("Employee salary is = ",self.salary)

ob = Employee("Manohar tiwari", 35, 50000)
ob.showEmployeeData()

'''


#
'''
class Account:
     rate_of_interest = 6
     def __init__(self, accountNo, balance):
          self.accountNo = accountNo
          self.balance = balance

     def showAccountDetails(self):
          print("Account no is = ",self.accountNo)
          print("Balance is = ",self.balance)

               
class FixedDeposit(Account):
     def setVaulue(self, principal, time):
          self.principal = principal
          self.time = time

     def getTime(self):
          return self.time
     
     def getPrincipal(self):
          return (self.principal)
     
     def simpleInterest(self):
          SI = (self.principal*self.rate_of_interest*self.time)/100
          print("simple interest is: ",SI)

ob = FixedDeposit(209876453, 300000.0)
ob.showAccountDetails()
ob.setVaulue(10000, 2)
print("Rate is interest is = ",FixedDeposit.rate_of_interest,"%")
print("Time is = ",ob.time)
print("Principal is = ",ob.principal)
ob.simpleInterest()

'''


#
'''
class Super:
     def __init__(self,a):
          self.a = a
     def func(self):
          print("a = ",self.a)

class Base(Super):
     def __init__(self, a, b):
          super().__init__(a)
          self.b = b
     def function(self):
          super().func()
          print("b = ",self.b)

obj = Base(4,5)
obj.function()

'''


'''
# Define class Account with instance object variable balance with initial value as 0. Provide withdraw and deposit methods.
class Account:
    def __init__(self):
        self.balance = 0 # instance object variable balance with initial value as 0

    def withdraw(self, amount):
        if amount > self.balance: # check if the amount is more than the balance
            print("Insufficient funds") # print an error message
        else:
            self.balance -= amount # subtract the amount from the balance
            print("Withdrew",amount,", new balance is",self.balance) # print a confirmation message

    def deposit(self, amount):
        self.balance += amount # add the amount to the balance
        print("Deposited",amount,", new balance is",self.balance) # print a confirmation message

# Define a subclass MinimumBalanceAccount of Account with provided minimum balance. Override withdraw method according to minimum balance condition.
class MinimumBalanceAccount(Account):
     def __init__(self, minimum_balance):
          super().__init__() # call the parent class constructor
          self.minimum_balance = minimum_balance # set the minimum balance attribute

     def withdraw(self, amount):
          if self.balance - amount < self.minimum_balance: # check if the withdrawal would violate the minimum balance condition
               print("Cannot withdraw below minimum balance of",self.minimum_balance) # print an error message
          else:
               super().withdraw(amount) # call the parent class method

ob = MinimumBalanceAccount(500)
# ob.deposit(100000)
ob.withdraw(10000)

'''



# Define a class Polygon with instance object variables to store number of sides and a list of n side length values
class Polygon:
    def __init__(self, n, *lengths):
        self.n = n # number of sides
        self.lengths = lengths # list of side length values

# Define a subclass Triangle of Polygon with instance methods getArea()
class Triangle(Polygon):
    def __init__(self, *lengths):
        super().__init__(3, *lengths) # call the parent constructor with n = 3

    def getArea(self):
        s = sum(self.lengths) / 2 # semi-perimeter
        a, b, c = self.lengths # unpack the side lengths
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # square root of the product
        return area
                 
obj = Triangle(10, 20, 30)
print("Area of Polygon is",obj.getArea())