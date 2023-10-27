import os
def writing(filename, text):
     f = open(filename, "w")
     f.write(text)
     f.close()

def append(filename, text):
     f = open(filename, "a")
     f.write(text)
     f.close()

def reading(filename):
     try:
          f = open(filename, "r")
          text = f.read()
          print(text)
          f.close()
     except FileNotFoundError:
          print("File nor found error")

def search(filename, word):
     try:
          f = open(filename,"r")
          line_count = 0
          for line in f.readlines():
               line_count+=1
               strlist = line.split(' ')
               word_count = 0
               for w in strlist:
                    word_count+=1
                    if word == w:
                         return(line_count, word_count)
               
          else:
               return None
          f.close()

     except FileNotFoundError:
          print("File not found")

def modify(filename, oldword, newword):
     t = search(filename, oldword)
     if t != None:
          mylist = []
          try:
               f = open(filename,"r")
               for line in f.readlines():
                    line = line.replace(oldword, newword)
                    mylist.append(line)
               f.close()
               f = open(filename, "w")
               f.write(''.join(mylist))
               f.close()
          except FileNotFoundError:
               print("File not found")
     
     else:
          print("Search Faild")

def delete(filename, oldword, newword=''):
     t = search(filename, oldword)
     if t != None:
          mylist = []
          try:
               f = open(filename,"r")
               for line in f.readlines():
                    line = line.replace(oldword, newword)
                    mylist.append(line)
               f.close()
               f = open(filename, "w")
               f.write(''.join(mylist))
               f.close()
          except FileNotFoundError:
               print("File not found")
     
     else:
          print("Search Faild")


# writing("file.txt", "Bhagwat katha")
# append("file.txt", "radhe radhe")
# reading("file.txt")
# modify("file.txt", "Bhagwat","BHAGWAT")
# delete("file.txt", "radhe")
# os.rename("file.txt", "f.txt")          #rename our file name
# os.remove("f.txt")                 #delete our file
