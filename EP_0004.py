def isPalindromic(num):
    numString = str(num)
    numStringReversed = numString[::-1]
    if numString == numStringReversed:
        return True
    else:
        return False

max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if isPalindromic(i * j) == True:
            if (i * j) > max:
                max = i * j

print(max)