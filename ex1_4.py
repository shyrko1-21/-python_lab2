# Найдите произведение элементов списка с нечетными номерами. 
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.

import random

lst = [random.randint(0, 10) for _ in range(10)]
print(f"Исходный список: {lst}")

p = 1
for i in range(len(lst)):
    if i % 2 != 0:
        p *= lst[i]
print(f"Произведение элементов списка с нечетными номерами: {p}")

max = max(lst);
while max in lst:
    lst.remove(max)

print(f"Максимальный элемент: {max}")
print(f"Список после удаления всех элементов, равных максимальному: {lst}")