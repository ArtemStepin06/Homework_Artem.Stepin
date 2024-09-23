import numpy as np

def mnk(x, y):
    x = np.array(x)
    y = np.array(y)

    xm = np.mean(x)
    ym = np.mean(y)


    numerator = np.sum((x - xm) * (y - ym))
    denominator = np.sum((x - xm) ** 2)

    a = numerator / denominator
    b = ym - a * xm

    return a, b


x_array = list(map(float, input().split()))
y_array = list(map(float, input().split()))

a, b = mnk(x_array, y_array)

print(f"y = {a}x + {b}")