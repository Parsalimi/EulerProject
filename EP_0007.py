from math import sqrt

# Setting
n = 10001# n th Number
# Varible
num = 0
counter = 0

# Code
def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(sqrt(n)+1), 2):
        if n % k == 0:
            return False
    return True


while counter <= (n - 1):
    num += 1
    if isPrime(num) == True:
        counter += 1

print(num)