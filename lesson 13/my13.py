import os

base_path = os.path.dirname(__file__)
file_path = f'{base_path}/data.txt'
new_file_path = f'{base_path}/data3.txt'

# data_file = open('data.txt', 'r')
# data_file.read()
# data_file.close()

def read_file():
    with open(file_path, 'r') as data_file:
        for i in data_file.readlines():
            yield i

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)