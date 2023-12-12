a = []
result = 0
for i in range(1,51):
    a.append(i)
for j in range (len(a)):
    if a[j] % 2 == 0:
        result += a[j]**1/2
print (result)