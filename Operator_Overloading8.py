class LessThen:
     def __init__(self, n):
          self.num = n
     def __lt__(self, other):
          if(self.num<other.num):
               return True
          else:
               return False
     
n1 = LessThen(6)
n2 = LessThen(5)
if(n1<n2):
     print("Number1 is less then number2")
else:
     print("Number2 is less then number1")
