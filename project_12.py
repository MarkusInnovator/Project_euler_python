import math

def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(n // i)
    return factors

def generate_triangle_numbers(n):
    triangle_numbers = []
    for i in range(1, n + 1):
        T_n = i * (i + 1) // 2
        triangle_numbers.append(T_n)
    return triangle_numbers

n=1
while True:
    a=generate_triangle_numbers(n)
    for i in a:
        if len(find_factors(i))==50:
            print(i)
    n+=1



