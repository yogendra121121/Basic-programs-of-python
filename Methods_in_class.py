class A:
     def __init__(self, a, b):   # instance method
          self.a = a
          self.b = b
     def f1(self):               # instance method
          print(self.a, self.b)

     @staticmethod
     def sm():       # static method
          print("This is a static method")

     @classmethod
     def cm(cls):    # class method
          print("this is a class method")


obj = A(4, 6)
obj.f1()    # f1(obj)

# static method call
A.sm()
#obj.sm()

# class method call
# A.cm()    # cm(A)
obj.cm()    # cm(A)

