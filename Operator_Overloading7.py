class Modulo:
     def __init__(self,n):
          self.num = n
     def __mod__(self, other):
          return (self.num%other.num)

n1 = Modulo(5)
n2 = Modulo(4)
n3 = n1%n2
print("negetive value is:",n3)