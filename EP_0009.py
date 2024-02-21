a = 1
b = 2

def isPythagorean(x, y, z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False
    
def abbbc(x, y, z):
    if x < y and y < z:
        return True
    else:
        return False
    
def giveMeC(x, y):
    return 1000 - (x + y)

def possibleB(x):
    for i in range(1000, x - 1, -1):
        if abbbc(x, i, giveMeC(x, i)) == True:
            return i
        
for j in range(a, 1000):
    for i in range(b, possibleB(a) + 1):
        if isPythagorean(j, i, giveMeC(j, i)) == True:
            print(j, i, giveMeC(j, i))
            break