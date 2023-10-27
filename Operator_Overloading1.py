class Subtraction:
     def __init__(self, n):
          self.num = n
     
     def __sub__(self, other):           # magic function
          return (self.num - other.num)
     
n1 = Subtraction(35)
n2 = Subtraction(45)
n3 = n1-n2    #  n1.__sub__(n2)
print("Subraction of two object is = ",n3)
        