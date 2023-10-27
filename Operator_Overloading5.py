class Equal:
     def __init__(self, n):
          self.num = n

     def __eq__(self, other):
          if (self.num == other.num):
               return True
          else:
               return False
     
m1 = Equal(45)
m2 = Equal(45)

if(m1==m2):      
     print("Numbers are equal")
else:
     print("Numbers are not equal")