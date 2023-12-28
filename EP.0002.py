n = int(input("please enter your number: "))
a = [1,2]
sum = 0
for i in range(1, n-1):
    a.append(a[i-1]+a[i])
    sum = sum + a[i+1]
print(3+sum)