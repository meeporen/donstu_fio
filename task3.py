x = input()
y = input()
if (int(x) < 0) and (int(y) < 0):
    x = abs(int(x))
    y = abs(int(y))
else:
    x = int(x)+1
    y = int(y)+1
print (x,y)