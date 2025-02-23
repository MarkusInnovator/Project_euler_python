def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0   
for i in range(0, 100000000):
    if is_prime(i):
        count += 1
        if count == 10001:
            print(i)
            break

             
             
             
