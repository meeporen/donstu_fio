def f(n):
    return str(n % 10) + " " + f(n // 10) if n else ""
print(f(12345))
