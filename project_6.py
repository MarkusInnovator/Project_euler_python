def sum_the_squares(num):
    sum=0
    for i in range(1,num+1):
        sum= sum + (i * i)
    return sum

def square_sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return (sum*sum)

print(square_sum(100))
print(sum_the_squares(100))
print(square_sum(100)-sum_the_squares(100))
