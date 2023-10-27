#conditional casing

x = int(input("Enter any value"))

match x:
     case x if type(x) == int:
          print("Value is int type")

     case x if type(x) == float:
          print("Value is float type")

     case x if type(x) == complex:
          print("Value is complex type")

     case x if type(x) == bool:
          print("Value is bool type")

     case _:
          print("default")
     