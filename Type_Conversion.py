print("Other data elements conversion into int:-")
print(int(2.4))
print(int("45"))
# print(int("657.8")) error
print(int(True))
print(int(False))

print("\nOther data elements conversion into float")
print(float(9))
print(float("345.56"))
print(float("56"))
print(float(True))
print(float(False))

print("\nOther data elements conversion into complex")
print(complex("3+6j"))
print(complex("3.8"))
print(complex(6.7))
print(complex(5.5))
print(complex(True))
print(complex(False))

print("\nOther data elements conversion into bool")
print(bool(45))
print(bool(5.8))
print(bool(-6))
print(bool(0))
print(bool(4+5j))
print(bool("abc"))   #every non empty string is true
print(bool(""))     #every empty string is flase
