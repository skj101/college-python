# Sanu K Joseph
def Fib(n):
   if n <= 1:
       return n
   else:
       return (Fib(n - 1) + Fib(n - 2))

for i in range(int(input("Enter the Value of n: "))):
   print(Fib(i),end = " ")
print()
