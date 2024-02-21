def triangle(x):
    sum_triangle = 0
    for i in range(1, x+1):
        sum_triangle += i
    return sum_triangle

def divisor(x):
    list_divisor = []
    for i in range(1, x + 1):
        if x % i == 0:
            list_divisor.append(i)
    return list_divisor
    
y = 1
while True:
    if len(divisor(triangle(y))) > 500:
        print(y, triangle(y))
        break
    y += 1