class Division:
     def __init__(self, n):
          self.num = n

     def __truediv__(self, other):
          return(self.num/self.num)
     
m1 = Division(5)
m2 = Division(5)
m3 = m1/m2
print("division of two object is:",m3)