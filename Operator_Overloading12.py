class Division:
     def __init__(self, n):
          self.num = n

     def __floordiv__(self, other):
          return(self.num//self.num)
     
m1 = Division(6)
m2 = Division(5)
m3 = m1//m2
print("floor division of two object is:",m3)