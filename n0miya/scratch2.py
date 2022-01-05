# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)

# usin = int(input())
# for i in range(usin):
#     print(fib(i))

import turtle as t

for i in range(6):
    t.fd(100)
    t.lt(60)

# t.mainloop()
t.exitonclick()