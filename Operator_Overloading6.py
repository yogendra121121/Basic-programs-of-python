class Negate:
     def __init__(self,n):
          self.num = n
     def __neg__(self):
          return (-self.num)

n = Negate(5)
n = -n
print("negetive value is:",n)