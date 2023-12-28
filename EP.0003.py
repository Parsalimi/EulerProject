# Problem 3
# Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import sqrt
#n = 13195
n = 600851475143

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(sqrt(n)+1), 2):
        if n % k == 0:
            return False
    return True

for i in range(1, n+1):
    if isPrime(i) == True and n%i==0:
        print(i)

# def primeFactor(number):
#     isPrimeFactor = True
#     if number == 1:
#         isPrimeFactor = False
#         return isPrimeFactor
#     else:
#         counter = 0
#         for i in range(1, number+1):
#             if number % i == 0:
#                 counter += 1
#         if counter > 2:
#             isPrimeFactor = False
#         return isPrimeFactor

# def Counter(number):
#     counterList = []
#     for i in range(1, number+1):
#         if number % i == 0:
#             counterList.append(i)
#     return counterList
#
# counterList = Counter(n)
# primeCounters = []
# for i in counterList:
#     if isPrime(i) == True:
#         primeCounters.append(i)
#
# print(primeCounters)