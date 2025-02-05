from functools import reduce


user_input = ''
while user_input != ' ':
    user_input = input('Введите действие: ')
    if user_input == 'exit':
        break
    elif '+' in user_input:
        user_input = user_input.split('+')
        user_input = list(map(int, user_input))
        print(f'Результат: ', sum(user_input))
    elif '-' in user_input:
        user_input = user_input.split('-')
        user_input = list(map(int, user_input))
        result_user_input = reduce(lambda x, y: x - y, user_input)
        print(f'Результат: ', result_user_input)
    elif '/' in user_input:
        user_input = user_input.split('/')
        user_input = list(map(int, user_input))
        result_user_input = reduce(lambda x, y: x / y, user_input)
        print(f'Результат: ', result_user_input)
    elif '*' in user_input:
        user_input = user_input.split('*')
        user_input = list(map(int, user_input))
        result_user_input = reduce(lambda x, y: x * y, user_input)
        print(f'Результат: ', result_user_input)
    else:
        print('К сожалению эту операцию я не могу выполнить :(')




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