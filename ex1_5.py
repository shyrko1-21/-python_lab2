# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент. 

import random

lst = [random.randint(-10, 10) for _ in range(10)]
# lst = [9,5,7,1,3]
print(f"Исходный список: {lst}")
try:
    print(f"Наименьший четный элемент: {min([i for i in lst if i % 2 == 0])}")
except:
    print(f"Четные элементы отсутсвуют. Первый элемент: {lst[0]}")