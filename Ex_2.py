# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

user_length = int(input('Enter the length of list: ')) # Блок инциализации списка
list_my = list(range(1, user_length+1))
for i in list_my:
    list_my[i-1] = random.randint(1, 9)

# Блок умножения первого и последнего элементов и 
# далее по порядку возрастания и убывания соответсвенно
new_list = [] 
for i in range(user_length // 2):
    print(i)
    new_list.append(list_my[i] * list_my[len(list_my) - i - 1])
if len(list_my) % 2 != 0:
    new_list.append(list_my[len(list_my) // 2] * list_my[len(list_my) // 2])

print(f'{list_my} => {new_list}')