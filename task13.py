a = [[1,-1],[2,-3]]
sum = 0
sum_spisok = []
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if a[i][j] > 0:
            sum +=a[i][j]
sum_spisok.append(sum)
print(sum_spisok)