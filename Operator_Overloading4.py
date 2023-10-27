class NotEqual:
     def __init__(self, n):
          self.num = n

     def __ne__(self, other):
          if (self.num != other.num):
               return True
          else:
               return False
     
m1 = NotEqual(5)
m2 = NotEqual(45)

if(m1!=m2):
     print("Numbers are not equal")
else:
     print("Numbers are equal")