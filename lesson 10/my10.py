# def func(test_func):
#     print('start')
#     test_func()
#     print('stop')
# def func_test1():
#     print('test1')
# def func_test2():
#     print('test2')
#
# func(func_test2)
# func(func_test1)


# def add_text(func):
#
#     def wrapper():
#         print('start')
#         func()
#         print('stop')
#     return wrapper
#
# def func_test1():
#     print('test1')
# func_test1 = add_text(func_test1)
# func_test1()
# def func_test2():
#     print('test2')
#
# func_test2 = add_text(func_test2)
# func_test2()

# def add_text(func):
#
#     def wrapper():
#         print('start')
#         func()
#         print('stop')
#     return wrapper
#
# @add_text
# def func_test1():
#     print('test1')
#
# @add_text
# def func_test2():
#     print('test2')
# @add_text
# def calc(x):
#     print(x * 2)
#
# calc(4)
# func_test2()

def add_text(func):

    def wrapper(*args):
        print('start')
        func(*args)
        print('stop')
    return wrapper


@add_text
def calc(x):
    print(x * 2)

@add_text
def calc2(x, y):
    print(x * y)

calc(2)
calc2(3, 5)