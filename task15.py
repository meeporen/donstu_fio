import random 

def min(matrix):
    min_=100000
    count_strok = 0
    count_stolb = 0
    for k in range(len(matrix)):
        for i in range(len(matrix[k])):
            if matrix[k][i] < min_:
                min_ = matrix[k][i]
                count_strok = k+1
                count_stolb = i+1
    return min_, count_strok, count_stolb





matrix1 = list()
for i in range(1,6):
    temp = []
    for j in range(1,11):
        temp.append(random.randint(1,9))
    matrix1.append(temp)
matrix2 = list()
for i in range(1,11):
    temp = []
    for j in range(1,5):
        temp.append(random.randint(1,9))
    matrix2.append(temp)
print (matrix1)
print (matrix2)
print(min(matrix1))
print(min(matrix2))
