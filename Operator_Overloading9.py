class GreaterThen:
     def __init__(self, n):
          self.num = n
     def __gt__(self,other):
          if(self.num>other.num):
               return True
          else:
               return False
     
n1 = GreaterThen(4)
n2 = GreaterThen(5)
if(n1>n2):
     print("Number1 is greater then number2")
else:
     print("Number2 is greater then number1")
