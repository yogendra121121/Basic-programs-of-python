# write a generator to produce squares of first N natural numbers.

'''def NaturalSquare(n):
     for i in range(1,n+1):
          yield i*i

re = NaturalSquare(10)
for i in re:
     print(i,end=", ")
'''


# write a generator to produce first N prime numbers.


'''def primeNumbers(n):
     pass

re = primeNumbers(10)
for prime in re:
     print(prime, end=" ")

'''

# write a generator to produce first N terms of the fibbonacci series.
'''def fibbonacci(n):
     a, b = 0, 1
     for i in range(1,n+1):
          temp = b
          b = a+b
          a = temp
          yield b

re = fibbonacci(10)
for f in re:
     print(f, end=" ")

'''

    

