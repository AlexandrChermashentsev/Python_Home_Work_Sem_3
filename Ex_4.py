# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 44 -> 101100
# 3 -> 11
# 2 -> 10

def integer_fool_proof(user_string_number): # Защита от дурака. Возвращает целое положительное число
    while not user_string_number.isdigit() and user_string_number[0] != '-':
        user_string_number = input('Please, enter the INTEGER number! ')
    else:
        user_string_number = int(user_string_number)
    return abs(user_string_number)

def reverse_string(string): # Функция переворачивания строки
    return string[::-1]

def from_ten_to_two(int_nbr_10): # Функция перевода из десятичной в двоичную систему. возвращает строку
    str_2 = ''
    while int_nbr_10 >= 2:
        str_2 += str(int_nbr_10 % 2)
        int_nbr_10 //= 2
    str_2 += str(int_nbr_10)
    return str_2

number_10 = integer_fool_proof(input('Enter the integer number: '))
number_2 = from_ten_to_two(number_10)

print(f'{number_10} -> {reverse_string(number_2)}')
