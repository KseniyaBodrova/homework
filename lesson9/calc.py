from functools import reduce

while True:
    user_input = input('Введите действие: ')

    if user_input == 'exit':
        break
    try:
        if '+' in user_input:
            result = list(map(int, user_input.split('+')))
            end_result = reduce(lambda x, y: x + y, result)

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
        print(f'Ошибка: на 0 делить нельзя, вы ввели {user_input}')

    except ValueError:
        print(f'Ошибка: введите корректные числа!, вы ввели {user_input}')

