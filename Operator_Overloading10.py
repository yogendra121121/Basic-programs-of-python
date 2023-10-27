class GreaterThenEqualTo:
     def __init__(self, n):
          self.num = n
     def __ge__(self,other):
          if(self.num>=other.num):
               return True
          else:
               return False
     
n1 = GreaterThenEqualTo(14)
n2 = GreaterThenEqualTo(9)
if(n1>=n2):
     print("Number1 is greater then equal to number2")
else:
     print("Number2 is greater then equal to number1")