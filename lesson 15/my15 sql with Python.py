import sqlite3

# Используем сырую строку для пути
# db_path = r'/Users/ksenia/Developer/local_db.sqlite'
# db = sqlite3.connect(db_path)
# db.row_factory = sqlite3.Row

# # Подключение к базе данных
# try:
#     db = sqlite3.connect(db_path)
#     print('Подключение успешно!')
# except sqlite3.OperationalError as e:
#     print('Ошибка подключения: {e}')
cursor = db.cursor()
# Запрос для получения списка всех таблиц
cursor.execute('SELECT name FROM sqlite_master WHERE type="table";')
tables = cursor.fetchall()

# Выводим список таблиц
print("Таблицы в базе данных:")
for table in tables:
    print(table[0])

# Выводим все строки таблицы Printer
cursor.execute('SELECT * FROM Printer')
data = cursor.fetchall()
print(data)
for row in data:
    print(dict(row))

# Выводим ОДИН результат(строку) из таблицы Printer
cursor.execute('SELECT * FROM Printer WHERE model = "1111"')
data2 = cursor.fetchone()
print(dict(data2))

# ## НЕ защищенный запрос от инъекций. Не используйте .format() для SQL-запросов
# print('новый запрос1')
# query = "SELECT * FROM Printer WHERE color = '{0}' AND price = '{1}'"
# cursor.execute(query.format(input('color'), input('price')))
# data4 = cursor.fetchall()
# for row in data4:
#     print(dict(row))
#
# ## Защищенный запрос от инъекций - через параметризованный запрос
# ## query = "SELECT * FROM Printer WHERE color = ? AND price = ?"
# ## cursor.execute(query, (color, price))
# print('новый запрос2')
# query = "SELECT * FROM Printer WHERE color = ? AND price = ?"
# cursor.execute(query, (input('color'), input('price')))
# for row in cursor.fetchall():
#     print(dict(row))

## Запрос на изменение в БД
print('новый запрос3')
cursor.execute("INSERT INTO Printer (code, model, color, type, price) VALUES (3, '1276', 'n', 'Laser', 250)")
cursor.execute("INSERT INTO Printer (code, model, color, type, price) VALUES (2, '1277', 'n', 'Laser', 255)")
db.commit()
# Закрытие соединения
db.close()

