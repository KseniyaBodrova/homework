# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance
#
#     def add(self, credit_amount):
#         self.credit_amount = credit_amount
#         result = self.balance + credit_amount
#         self.balance = result
#         return print(result)
#
#     def withdraw(self, write_off_amount):
#         self.write_off_amount = write_off_amount
#         if self.balance >= self.write_off_amount:
#             result = self.balance - write_off_amount
#             self.balance = result
#             print(result)
#         else:
#             print('Error')
#
# card = BankAccount(34343434, 300)
# card.add(230)
# print(card.balance)
# card.withdraw(560)
# print(card.balance)
# card.withdraw(90)
# print(card.balance)


class Person:
    def __init__(self, age):
        self._age = age

tom = Person(20)
print(tom._age)



