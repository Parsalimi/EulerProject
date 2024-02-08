flag = True
n = 20
while flag:
    n += 2
    counter = 0
    for i in range(3, 20 + 1):
        if n % i == 0:
            counter += 1
    
    if counter == 19:
        flag = False

print(n)