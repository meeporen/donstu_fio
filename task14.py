def bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
a = 1
b = 2
c = 3
 

 
print(bin(a), bin(b), bin(c))