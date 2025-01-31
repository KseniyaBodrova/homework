import datetime

# my_list = [1, 2, 3, 4, 5]
# def mult2(x):
#     return x * 2
#
# new_list = map(mult2, my_list)
# print(type(new_list))
# print(list(new_list))
#



def flip_flop(x):
    return 'flop' if x == 'flip' else 'flip'
print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'

def flip_flop(x):
    if x == 'flip':
        return 'flop'
    else:
        return 'flip'
print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'

my_list = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, my_list)
print(list(new_list))

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'
python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')
human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)


