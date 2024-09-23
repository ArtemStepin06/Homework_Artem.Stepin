def fibonacci(n):
    if n <= 0:
        print("Ошибка")
    elif n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        print(b)


n = int(input())  
print(fibonacci(n))