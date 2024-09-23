a = input().split()
size = int(a[0])
symb = a[1]


def triangle(size, symb):
    for i in range(size // 2 + size % 2):
        print(symb * (i + 1))
    for i in range(size // 2, 0, -1):
        print(symb * i)


triangle(size, symb)
