from functools import reduce
from sys import excepthook

user_input = ''
while True:
    user_input = input('Введите действие: ')

    if user_input == 'exit':
        break
    try:
        if '+' in user_input:
            result = list(map(int, user_input.split('+')))
            end_result = sum(result)

        elif '-' in user_input:
            result = list(map(int, user_input.split('-')))
            end_result = reduce(lambda x, y: x - y, result)

        elif '/' in user_input:
            result = list(map(int, user_input.split('/')))
            end_result = reduce(lambda x, y: x / y, result)

        elif '*' in user_input:
            result = list(map(int, user_input.split('*')))
            end_result = reduce(lambda x, y: x * y, result)

        else:
            print('К сожалению эту операцию я не могу выполнить :(')
            continue

        print(f'Результат: {end_result}')

    except ZeroDivisionError:
        print('Ошибка: на 0 делить нельзя')

    except ValueError:
        print('Ошибка: введите корректные числа!')


# def summa_calc(a, b):
#     return a + b
# def subtraction_calc(a, b):
#     return a - b
# a = int(input('Введи первое число'))
# opereator_calc = input('Введи оператор')
# b = int(input('Введи второе число'))

# print(a)
# print(b)
# if opereator_calc == '+':
#     print(summa_calc(a, b))
# else:
#     print(subtraction_calc(a, b))