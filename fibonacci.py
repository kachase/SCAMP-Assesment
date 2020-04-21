//a program that prints out a fibonacci sequence given a number


def Fib(n):
 if n<0:
 print("invalid!)
 elif n==0:
 return 0
 elif n==1:
 return 1
 
 else :
 return Fib(n-1) + Fib(n-2)

print(Fib(11))
