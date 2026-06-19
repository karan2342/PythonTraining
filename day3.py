def fib(n):
  if n<1:
    return 1
  return fib(n-1) + (n-2)

for i in range(10):
  print(fib(i), end=" ")