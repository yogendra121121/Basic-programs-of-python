class Line:
     def __init__(self, l):
          self.length = l
     def show_length(self):
          print("Length = ",self.length)
     def __add__(self, other):           # magic function
          return (self.length+other.length)
l1 = Line(35)
l2 = Line(45)
l3 = l1+l2
print(l3)
l1.show_length()
        
'''
Other magic function

1. -    __sub__
2. /    __truediv__
3. *    __mul__
4. !=   __ne__
5. ==   __eq__
6.unary - __neg__
7. %    __mod__
8. <    __lt__
9. >    __gt__
10. <=  __le__
11. >=  __ge__
12. //  __floordiv__
13. >>  __rshift__

'''