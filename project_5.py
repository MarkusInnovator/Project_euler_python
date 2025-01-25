def is_divisible_by_1_to_10(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

for number in range(1, 900000000):
    if is_divisible_by_1_to_10(number):
        print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 10 is:", number)
        break
