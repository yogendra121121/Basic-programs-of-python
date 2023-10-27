# Area of recangle program with the help of classes and object in python

class Rectangle:
     def setDimensions(self, length, breadth):
          self.length = length
          self.breadth = breadth
     def showDimensions(self):
          print("Length = ",self.length)
          print("Breadth = ",self.breadth)
     def getArea(self):
          print("Area of rectangle is = ",self.length*self.breadth)

ob = Rectangle()
ob.setDimensions(4,7)
ob.showDimensions()
ob.getArea()


# variable length argument with the help of class and object in python
''' 
class Team:
     def setnames(self, *t):
          self.t = t
     def getnames(self):
          return list(self.t)

ob = Team()
ob.setnames("rs","sd","vk","sy","rj","ap","ra","yc","ms","jb","ms")
print("list of names is: ",ob.getnames())

'''


#
'''
class Book:
     def __init__(self, title, price):
          self.title = title
          self.price = price
     def showbook(self):
          print("Book's title is = ",self.title)
          print("Book's price is = ",self.price)

ob = Book("Introduction to python", 500.25)
ob.showbook()

'''


#
'''
class Circle:
     def setRadius(self, radius):
          self.radius = radius
     def getRadius(self):
          return self.radius
     def getArea(self):
          return(3.14*self.radius**2)
     def getCircumference(self):
          return(2*3.14*self.radius)
     
ob = Circle()
ob.setRadius(4)
print("Radius is= ",ob.getRadius())
print("Area of circle is = ",ob.getArea())
print("Circumference of circle is = ",ob.getCircumference())

'''