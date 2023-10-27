'''
def gene():
     yield 10
     yield 20
     yield 30
     yield 40

g=f1()
for e in g:
     print(e)

'''

def fun(n):
     i =  1
     while i<=n:
          yield i
          i += 1

g=fun(10)
for e in g:
     print(e,end=' ')