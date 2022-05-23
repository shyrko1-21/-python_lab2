# В матрице найти номер строки, сумма чисел в которой максимальна.

import random, numpy as np

lst = np.array([[random.randint(0, 10) for _ in range(3)],
    [random.randint(0, 10) for _ in range(3)],
    [random.randint(0, 10) for _ in range(3)]])

print(f"Матрица чисел:\n {lst}")

s = 0
for i in range(len(lst)):
    if sum(lst[i]) > s:
        s = sum(lst[i])
        rowNumber = i

print(f"Номер строки, сумма чисел в которой максимальна: {rowNumber}, сумма чисел: {s}")