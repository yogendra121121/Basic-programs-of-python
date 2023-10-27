class Multiply:
     def __init__(self, n):
          self.num = n

     def __mul__(self, other):
          return(self.num*self.num)
     
m1 = Multiply(2)
m2 = Multiply(5)
m3 = m1*m2              # m1.__mul__(m2)
print("multiply of two object is:",m3)