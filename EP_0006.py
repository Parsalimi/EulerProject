# Setting
LastNum = 100

# Varible
sumSquare = 0
squareSum = 0

### Code
for i in range(1, LastNum + 1):
    sumSquare += i ** 2

for i in range(1, LastNum + 1):
    squareSum += i
squareSum **= 2

print(squareSum - sumSquare)