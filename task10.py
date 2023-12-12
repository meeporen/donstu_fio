num = [7,8,3,2,4,3]
tmp = 0
for i in range(len(num)-1):
    if (num[i] > 1) and(num[i] > num[i+1]) and (num[i] > num[i-1]):
        print(i)