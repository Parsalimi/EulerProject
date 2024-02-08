# Problem 0001
# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 bellow 1000
i=1
sum = 0
num = 1000
while i< 1000:
    if ((i%3==0) or (i%5==0)):
        sum_ +=i
    i+=1
print(sum)