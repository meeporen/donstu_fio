import math
n = int(input())
x = int(input())
result = 0
for i in range(1,n):
    result += 1/math.factorial(i)+math.sqrt(abs(x))
print(result)
