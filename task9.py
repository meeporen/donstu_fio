num = [1,2,3,4,5,6,7,8,9,1,1,1,2,2,2,3,4,4]
min = 1000000
for i in range(len(num)):
    if num[i] < min:
        min = num[i]
for i in range(len(num)):
    if num[i] == min:
        num[i] = 0
print(num)