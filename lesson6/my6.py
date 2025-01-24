# На вход программе подаются две строки:
# - в первой строке задается слово s;
# - во второй - три целых числа a, b, c (каждое число находится в диапазоне [-len(s); len(s)-1])
# Выведите на экран новое слово, образованное символами с индексами a, b, c (в указанном порядке)

# s = 'информатика'
# word_len = len(word)
# print(word_len)
# a, b, c = 2, 3, 4
# print(s[-1])
# print(s[10])

# print(s[a] + s[b] + s[c])
# print(s[a:c + 1])
# print(s.)

# user_input = int(input('number'))
# if user_input == 1:
#     print('one')
# elif user_input == 2:
#     print('two')
# else: print('more')

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'
text = text.split()
fin_text = []
for i in text:
    if 'o' in i:
        print(i)
    else:
        fin_text.append(i)
print(' '.join(fin_text))