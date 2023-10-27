class LessThenEqualTo:
     def __init__(self, n):
          self.num = n
     def __le__(self,other):
          if(self.num<=other.num):
               return True
          else:
               return False
     
n1 = LessThenEqualTo(14)
n2 = LessThenEqualTo(9)
if(n1<=n2):
     print("Number1 is less then or equal to number2")
else:
     print("Number2 is less then or equal to number1")