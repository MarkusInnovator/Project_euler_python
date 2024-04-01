def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

limit = 4000000
sum_even = 0
n = 0

# Berechnung der Fibonacci-Zahlen und Summe der geraden Zahlen
while fib(n) <= limit:
    if fib(n) % 2 == 0:
        sum_even += fib(n)
    n += 1

print("Die Summe der geraden Zahlen in der Fibonacci-Folge unter", limit, "ist:", sum_even)
