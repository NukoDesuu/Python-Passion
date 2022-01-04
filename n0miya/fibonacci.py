def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)
    
usin = int(input())
for i in range(usin):
    print(fib(i))