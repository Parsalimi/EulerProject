import math

def isPrime(x):
    if x == 2 or x == 3 or x == 5:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
    return True

sum = 0
for i in range(2, 2000000 + 1):
    if isPrime(i) == True:
        sum += i

print(sum)