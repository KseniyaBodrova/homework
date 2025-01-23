# my_test_list = [1, 2]
# my_test_tupple = (4, 5, 6)
# a = my_test_list[0]
# b = my_test_list[1]
# c = my_test_tupple[0]
# d = my_test_tupple[1]
# e = my_test_tupple[2]
# a, b = my_test_list
# c, d, e = my_test_tupple
# print(a, b, c, d, e)

# list_a = [2, 5, 6, 7]
# print(list_a)
# print(list_a[1:2])
# print(list_a[:2])
# print(list_a[-1:-3:-1])
#
# text = 'My long long string. new'
# print(text[4])
# print(len(text))
# print(text.index("o"))
# print(text.index("lo"))
# print("My" in text)
# print(text.count("n"))
# print(text[0:6])
# print(text.capitalize())
# new_index = text.index("new")
# print(text[0:1].lower() + text[1:new_index] + text[new_index:].title())
#
# text = text.replace("long", "short")
# print(text)
# text = " sort sort "
# print(text)
# print(text.strip())


# my_string = "some, little text"
# list_from_text = my_string.split(", ")
# print(list_from_text)
#
# new_sting = ['some', 'little', 'text']
# print(new_sting)
# new_sting = " ".join(new_sting)
# print(new_sting)
# print(type(new_sting))
# a = 'one'
# b = 'two'
# my_text = 'First word is ' + a + ', second word is ' + b
# print(my_text)

# Сравните пары слов, в ответе укажите знак: >, <, =
# "пар"и"steam"
a = "пар"
b = "steam"
print(">", a > b)
print("<", a < b)
print("=", a == b)
# На вход подается одна строка, в которой записаны фамилия и имя человека Pupkin Vasya
# Выведите эту же информацию, однако сначала имя, а потом фамилию.
user_name = "Pupkin Vasya"
a, b = user_name.split()
print(b, a)

