def prost(a):
    if a <= 1:
        return "Ошибка"
    b = []
    while a % 2 == 0:
        b.append(2)
        a //= 2
    for i in range(3, int(a**0.5) + 1, 2):
        while a % i == 0:
            b.append(i)
            a //= i
    if a > 2:
        b.append(a)
    return b


number = int(input())
print(prost(number))
