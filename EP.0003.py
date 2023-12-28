n = 13195

def primeFactor(number):
    isPrimeFactor = True
    if number == 1:
        isPrimeFactor = False
        return isPrimeFactor
    else:
        counter = 0
        for i in range(1, number+1):
            if number % i == 0:
                counter += 1
        if counter > 2:
            isPrimeFactor = False
        return isPrimeFactor

def Counter(number):
    counterList = []
    for i in range(1, number+1):
        if number % i == 0:
            counterList.append(i)
    return counterList

counterList = Counter(n)
primeCounters = []
for i in counterList:
    if primeFactor(i) == True:
        primeCounters.append(i)

print(primeCounters)