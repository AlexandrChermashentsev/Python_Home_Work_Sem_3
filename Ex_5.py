# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def integer_fool_proof(user_string_number): # Защита от дурака. возвращает положительное целое число
    while not user_string_number.isdigit() and user_string_number[0] != '-':
        user_string_number = input('Please, enter the INTEGER number! ')
    else:
        user_string_number = int(user_string_number)
    return abs(user_string_number)

def Fibonacci(number): # Вычесление чисел Фибоначчи, не через рекурсию
    if number == 0:
        fib = [0]
        return fib
    elif number == 1:
        fib = [0, 1]
        return fib
    else:        
        fib = list(range(number + 1))
        fib[0], fib[1] = 0, 1
        for i in range(2, len(fib)):
            fib[i] = fib[i-1] + fib[i-2]
        return fib

def Negative_And_Positive_List(list): # Функция которая "отзеркаливает" список
    result_list = []
    for i in range(len(list)):
        result_list.append(list[len(list) - i - 1] * (-1))
    for i in range(1, len(list)):
        result_list.append(list[i])
    return result_list



number = integer_fool_proof(input('Enter the integer number: '))
fib = Fibonacci(number)
negative_and_positive_fib = Negative_And_Positive_List(fib)
print(negative_and_positive_fib)
